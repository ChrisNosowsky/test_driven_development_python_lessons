Test-driven development is a way to write code on a very
repetitious cycle where core production functionality
corresponds to what you write in your test cases.

The test cases are meant to fail at first, you build your production
code to not make those tests fail. When your tests pass, you know your production code passes.
It is important to write very nitty-gritty, specific unit tests in order to make code compatible for all scenarios that could
arise.

In the bowling example, I test edge cases of rolling all strikes or rolling all gutters. I also test for the
occasional spares and strikes or just regular rolls between frames.
