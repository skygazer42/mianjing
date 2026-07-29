from __future__ import annotations  # 启用现代类型标注并保持旧解释器兼容。

import argparse  # 解析命令行传入的 Notebook 路径。
import ast  # 统计断言、输出调用和语法结构。
from io import StringIO  # 把代码字符串包装成 tokenizer 可读取的流。
from pathlib import Path  # 使用跨平台路径对象定位 Notebook。
import re  # 检查中文注释和教学章节关键词。
import tokenize  # 精确区分代码、字符串与同行注释。

import nbformat  # 读取并校验 Jupyter Notebook 的 nbformat 结构。


CHINESE_PATTERN = re.compile(r"[\u3400-\u9fff]")  # 定义中文字符检测范围。
REQUIRED_SECTIONS = ("真实案例", "基线", "结果解读", "失败案例")  # 定义案例驱动教学的必备章节。


def inspect_code_comments(source: str) -> list[int]:  # 返回缺少同行中文注释的有效代码行号。
    tokens = list(tokenize.generate_tokens(StringIO(source).readline))  # 对完整代码单元执行 Python 词法分析。
    code_lines: set[int] = set()  # 收集真正包含代码 token 的物理行。
    chinese_comment_lines: set[int] = set()  # 收集带中文同行注释的物理行。
    ignored = {tokenize.ENCODING, tokenize.ENDMARKER, tokenize.INDENT, tokenize.DEDENT, tokenize.NEWLINE, tokenize.NL}  # 定义不代表有效代码的 token。
    for token in tokens:  # 逐个检查词法 token 的类型和所在行。
        if token.type == tokenize.COMMENT:  # 单独处理 Python 注释 token。
            if CHINESE_PATTERN.search(token.string):  # 只认可真正包含中文解释的注释。
                chinese_comment_lines.add(token.start[0])  # 记录当前注释所在物理行。
        elif token.type == tokenize.STRING and token.start[0] != token.end[0]:  # 排除多行字符串正文对行号的干扰。
            continue  # 多行 Markdown 式字符串不算有效代码行。
        elif token.type not in ignored:  # 其余有效 token 都说明当前行存在代码。
            code_lines.add(token.start[0])  # 记录代码 token 的起始物理行。
    return sorted(code_lines - chinese_comment_lines)  # 返回所有没有中文同行注释的代码行。


def validate_notebook(path: Path) -> list[str]:  # 对单本 Notebook 执行教学和结构验收。
    errors: list[str] = []  # 收集全部错误，避免发现第一项后立即退出。
    notebook = nbformat.read(path, as_version=4)  # 按 nbformat 4 读取目标 Notebook。
    nbformat.validate(notebook)  # 先验证 Notebook JSON 与官方 schema 一致。
    code_cells = [cell for cell in notebook.cells if cell.cell_type == "code"]  # 提取所有代码单元供后续统计。
    markdown = "\n".join(cell.source for cell in notebook.cells if cell.cell_type == "markdown")  # 合并 Markdown 便于检查教学章节。
    if len(code_cells) < 6:  # 教学实验至少要覆盖输入、基线、实现、结果、失败和测试。
        errors.append(f"代码单元不足：{len(code_cells)} < 6")  # 记录代码单元数量不足。
    for section in REQUIRED_SECTIONS:  # 逐项检查四个必备教学章节。
        if section not in markdown:  # Markdown 未出现当前章节关键词时判定缺失。
            errors.append(f"缺少教学章节：{section}")  # 记录缺失章节供作者修正。
    assert_locations: list[tuple[int, int]] = []  # 保存每条断言所在的代码单元和物理行。
    visible_calls = 0  # 统计 print、display 与 pprint 等可见输出调用。
    output_cells = 0  # 统计磁盘中已经保存可见结果的代码单元。
    output_characters = 0  # 统计保存输出的大致文本规模以排除空壳输出。
    for code_index, cell in enumerate(code_cells, start=1):  # 按执行顺序检查每个代码单元。
        try:  # 捕获语法错误并继续报告其他 Notebook 问题。
            tree = ast.parse(cell.source)  # 将代码解析成 AST 以识别真实语句。
        except SyntaxError as error:  # 单独处理 Python 语法错误。
            errors.append(f"代码单元 {code_index} 语法错误：{error}")  # 记录语法错误位置和原因。
            continue  # 当前单元无法继续做 AST 统计。
        for node in ast.walk(tree):  # 遍历当前代码单元的全部 AST 节点。
            if isinstance(node, ast.Assert):  # 找到真正的 assert 语句而非字符串文本。
                assert_locations.append((code_index, node.lineno))  # 保存断言所在单元和行号。
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in {"print", "display", "pprint"}:  # 识别面向学习者的可见输出调用。
                visible_calls += 1  # 累加可见输出调用数量。
        if any(isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and node.value.value is Ellipsis for node in ast.walk(tree)):  # 禁止用省略号冒充实现。
            errors.append(f"代码单元 {code_index} 含未实现的省略号")  # 记录未完成实现。
        missing_comments = inspect_code_comments(cell.source)  # 检查当前单元每个有效代码行的中文注释。
        if missing_comments:  # 只在确有违规时追加错误。
            errors.append(f"代码单元 {code_index} 缺中文同行注释：{missing_comments[:8]}")  # 限制行号输出长度便于阅读。
        if any(token.type == tokenize.OP and token.string == ";" for token in tokenize.generate_tokens(StringIO(cell.source).readline)):  # 检测一行多语句的分号写法。
            errors.append(f"代码单元 {code_index} 使用分号压缩语句")  # 要求教学代码一行只表达一个动作。
        if cell.execution_count is None:  # 新标准要求保存可复现执行状态。
            errors.append(f"代码单元 {code_index} 未保存执行计数")  # 记录没有执行过的代码单元。
        if cell.outputs:  # 当前单元保存了至少一个 Jupyter 输出对象。
            output_cells += 1  # 累加带输出的代码单元数量。
            for output in cell.outputs:  # 逐个检查输出是否包含异常或有效文本。
                if output.output_type == "error":  # 保存的异常会误导学习者并破坏顺序执行。
                    errors.append(f"代码单元 {code_index} 保存了异常输出：{output.ename}")  # 记录异常类型。
                output_characters += len(str(output.get("text", "")))  # 统计 stream 或 execute_result 的文本长度。
                output_characters += len(str(output.get("data", {})))  # 统计富媒体输出的序列化规模。
    if not 4 <= visible_calls:  # 至少四处输出才能覆盖输入、过程、结果和失败案例。
        errors.append(f"可见输出调用不足：{visible_calls} < 4")  # 记录输出调用数量不足。
    if output_cells < 3:  # 至少三个单元应在打开 Notebook 时直接展示结果。
        errors.append(f"保存输出单元不足：{output_cells} < 3")  # 记录保存输出单元数量不足。
    if output_characters < 200:  # 过短输出通常只是“完成”字样而非教学结果。
        errors.append(f"保存输出内容过少：{output_characters} < 200")  # 记录输出内容规模不足。
    if len(assert_locations) > 8:  # 限制断言数量，避免再次退化为测试套件。
        errors.append(f"断言过多：{len(assert_locations)} > 8")  # 记录断言数量超标。
    if assert_locations and any(code_index != len(code_cells) for code_index, _ in assert_locations):  # 断言只能集中在最后的回归测试单元。
        errors.append(f"断言没有集中在最后代码单元：{assert_locations[:8]}")  # 记录前置断言的位置。
    return errors  # 返回当前 Notebook 的完整验收错误列表。


def main() -> int:  # 解析参数、执行批量验收并返回进程状态码。
    parser = argparse.ArgumentParser(description="验证案例驱动中文教学 Notebook")  # 创建命令行参数解析器。
    parser.add_argument("paths", nargs="+", type=Path, help="一个或多个 ipynb 文件或目录")  # 支持传入文件和目录混合列表。
    arguments = parser.parse_args()  # 读取用户传入的命令行参数。
    notebooks: list[Path] = []  # 收集去重后的目标 Notebook 路径。
    for path in arguments.paths:  # 逐个展开文件或目录参数。
        if path.is_dir():  # 目录参数需要递归查找全部 Notebook。
            notebooks.extend(sorted(path.rglob("*.ipynb")))  # 按路径排序保证输出稳定。
        else:  # 文件参数直接加入验收列表。
            notebooks.append(path)  # 保存显式指定的 Notebook 文件。
    notebooks = sorted(set(notebooks))  # 去重并固定批量验收顺序。
    failed = 0  # 统计未通过验收的 Notebook 数量。
    for notebook_path in notebooks:  # 逐本运行教学质量检查。
        errors = validate_notebook(notebook_path)  # 获取当前 Notebook 的所有错误。
        if errors:  # 有任一错误就输出失败详情。
            failed += 1  # 累加失败 Notebook 数量。
            print(f"FAIL {notebook_path}")  # 输出失败文件路径供直接定位。
            for error in errors:  # 逐条打印可操作的修正建议。
                print(f"  - {error}")  # 缩进显示当前错误详情。
        else:  # 当前 Notebook 满足全部新标准。
            print(f"PASS {notebook_path}")  # 输出通过状态供 CI 或人工审阅。
    print(f"SUMMARY total={len(notebooks)} passed={len(notebooks) - failed} failed={failed}")  # 汇总批量验收结果。
    return 1 if failed else 0  # 任何失败都返回非零状态码。


if __name__ == "__main__":  # 仅在直接执行脚本时进入命令行入口。
    raise SystemExit(main())  # 将验收结果转换为进程退出码。
