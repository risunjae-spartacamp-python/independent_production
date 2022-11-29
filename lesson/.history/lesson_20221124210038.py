from bs4 import BeautifulSoup


html = """
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>

<body>
    <h1>タイトル</h1>
    <h2>演習内容</h2>
    <ol id="step1" class="study-list">
        <li>Python</li>
        <li>HTML</li>
    </ol>
    <ol id="step2" class="study-list">
        <li>JS</li>
        <li>Ruby</li>
    </ol>

</body>

</html>

"""
soup = BeautifulSoup(html, "html.parser")
print(soup.h1.text)
