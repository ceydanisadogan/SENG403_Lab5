# SENG 403 · Lab 5 — Coverage and mutation testing

In this lab you measure the coverage of a small program. You write tests for the parts that no test runs. Then you use mutation testing to check how good your tests are.

**Today you may read the code. But the expected result of every test must come from the specification. You find the specification in the worksheet, in step A0.**

## Start the lab in GitHub Codespaces (recommended)

You do not need to install anything on your computer. Follow these steps:

1. Sign in to GitHub.
2. Click the **Fork** button at the top of this page. Then click **Create fork**. Now you have your own copy of the lab.
3. In **your fork**, click the green **Code** button. Open the **Codespaces** tab and click **Create codespace on main**.
4. Wait a few minutes. The first start installs Python, Java, Maven and the VS Code extensions. It also downloads the test tools. When the terminal says `Lab 5 is ready`, you can start.
5. Open the worksheet. In the Explorer on the left, right-click `SENG403_Lab5_Worksheet.html` and choose **Show Preview**. Then click the small globe icon at the top of the preview. This opens the worksheet in a normal browser tab. Your answers are saved in that browser tab, and the **Download my answers** button works there.
6. Open `SENG403_Lab5_Cheatsheet.html` in the same way, and keep it open in another tab.

**Save your work often.** Your code is safe in the codespace. But a codespace is deleted after some weeks without use. To keep your work, commit and push it to your fork: open the **Source Control** view on the left, write a short message, and click **Commit**, then **Sync Changes**.

A codespace uses your free monthly Codespaces hours. When you finish working, stop it: click **Codespaces** in the bottom-left corner and choose **Stop Current Codespace**.

## Choose one track

You work in Python **or** in Java. Choose one track at the top of the worksheet.

### Python track

Run these commands in the terminal, in the main folder of the lab:

```bash
pytest -v test_juicebar.py
```

The output says `5 passed`. This is the setup step.

```bash
pytest --cov=juicebar --cov-branch --cov-report=term-missing test_juicebar.py
```

This command measures coverage (Part A and Part B).

```bash
python mutation_run.py
```

This command runs mutation testing (Part C).

You can also run the tests from the **Testing** view (the flask icon on the left).

### Java track

Go to the `java` folder first:

```bash
cd java
```

```bash
mvn -q test
```

This command runs the tests. In the setup step, all 5 tests pass. The coverage report is in `target/site/jacoco/index.html`.

```bash
mvn -q test-compile org.pitest:pitest-maven:mutationCoverage
```

This command runs mutation testing (Part C). The report is in `target/pit-reports/index.html`.

To open an HTML report, right-click the file in the Explorer and choose **Show Preview**.

## Work on your own computer (optional)

You can also clone your fork and work on your own computer. For the Python track you need Python 3.10 or newer. Run `pip install -r requirements.txt` once. For the Java track you need JDK 17 or newer and Maven. The first Maven run needs the internet, because it downloads JUnit, JaCoCo and PIT.

## The files

| File | What it is |
|---|---|
| `SENG403_Lab5_Worksheet.html` | The worksheet. Follow its steps and write your answers in it. |
| `SENG403_Lab5_Cheatsheet.html` and `.pdf` | Words, rules and commands for the lab. |
| `juicebar.py` and `java/src/main/java/JuiceBar.java` | The code that you test. |
| `test_juicebar.py` and `java/src/test/java/JuiceBarTest.java` | The tests. You add your tests under **YOUR TESTS**. |
| `mutation_run.py` | A small mutation testing tool for the Python track. Do not change this file. |

## Hand in

Hand in three files:

1. the file that you get with the **Download my answers** button in the worksheet,
2. `test_juicebar.py` (or `JuiceBarTest.java`),
3. `juicebar.py` (or `JuiceBar.java`).
