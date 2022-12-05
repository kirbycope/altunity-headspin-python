# altunity-headspin-python
[AltUnity](https://altom.gitlab.io/altunity/altunitytester) enables UI test automation, by instrumenting games to get access and programmatically control the Unity objects.</br>
[Headspin](https://headspin.io/) is a Digital Experience AI Platform that combines a global device infrastructure, test automation, and ML-driven analytics. </br>
[Python](https://www.python.org/) is an interpreted high-level general-purpose programming language.

## Core Concepts
* [Behaviour Driven Development](https://en.wikipedia.org/wiki/Behavior-driven_development) is an agile software development process that encourages collaboration among developers, quality assurance testers, and customer representatives in a software project.
  * Stakeholders might be used to the User Story template; ["As a … I want … So that …"](https://martinfowler.com/bliki/UserStory.html)
  * Developers might be used to a unit test design pattern; ["Arrange, Act, Assert"](http://wiki.c2.com/?ArrangeActAssert)
  * Cucumber expresess functionality using keywords; ["Given, When, Then"](https://en.wikipedia.org/wiki/Given-When-Then)
* [Fluent Interface](https://en.wikipedia.org/wiki/Fluent_interface) is an object-oriented API whose design relies extensively on method chaining.
  * PageObect.someFunction()
  * PageOject.someElement().click()
* [Page Object Model](https://www.selenium.dev/documentation/en/guidelines_and_recommendations/page_object_models/) is a Design Pattern which has become popular in test automation for enhancing test maintenance and reducing code duplication. </br>
  * The "login" screen will have a "Login page object" that contains the selectors for elements on the page and functions that can be performed on that page.

## Getting Started
1. Install [Python3](https://www.python.org/downloads/)
1. Open the [integrated terminal](https://code.visualstudio.com/docs/editor/integrated-terminal)
1. Install dependencies noted in [requirements.txt](/requirements.txt)
   * In the integrated terminal run `pip3 install -r requirements.txt`
1. In the root folder create a new file called `.env`
1. Copy+Paste the following (changing the placeholder to your API Key)
   ```
   API_KEY="0123456789"
   ```
1. Save
1. Open `headspin.ini` and set your values
1. Save

## Run Tests

### AltUnity (Unity Mobile Apps)
[AltUnity](https://altom.gitlab.io/altunity/altunitytester) is a free, open source asset. Its main goal is to enable UI test automation, by instrumenting games to get access and programmatically control the Unity objects.</br>
The [apk](/trashcat.apk) is included as part of _this_ sample repo.

   * In the integrated terminal run `behave`

## Python Tips and Tricks

### Clear Dependencies

   * [mac] In the integrated terminal run `pip3 freeze | xargs pip uninstall -y`
   * [win] In the integrated terminal run `pip3 uninstall -y -r <(pip freeze)`

### Hide pycache from VS Code's Explorer
1. Open the [Command Pallete](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)
1. Search for and then select "Preferences: Open User Settings"
1. Seach for `files.exclude`
1. Select the "Add Pattern" button
1. Enter `**/__pycache__`
