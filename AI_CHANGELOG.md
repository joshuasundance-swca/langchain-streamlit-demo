# AI CHANGELOG
## [Updated requirements.txt for better package management](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/5085ade2d646a2670929e518e78b881ea2ffd0a5)
Tue Sep 26 23:14:05 2023 -0400
- Rolled back langchain package from version 0.0.301 to 0.0.300 to avoid a bug in langchain's chatanthropic.
- Pinned numpy to version 1.22.2 as suggested by Snyk to avoid a vulnerability.
- Reordered the packages for better readability.
## [Added numpy and tornado to requirements.txt to avoid vulnerabilities](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/3f0e220f9f77d561510dd04b09f1c3c509a5b28f)
Tue Sep 26 12:56:59 2023 +0000
- The numpy and tornado packages were added to the requirements.txt file. These packages are not directly required by our application but were added to avoid potential vulnerabilities as suggested by Snyk.
## [Updated token used for code checkout in GitHub workflow](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/b0c4e1ca12f86ea6113ee2c86d38c39d3035f395)
Tue Sep 26 08:56:55 2023 -0400
- In the GitHub Actions workflow file 'ai_changelog.yml', the personal access token used for checking out code has been updated. The token has been changed from 'PAT' to 'WORKFLOW_GIT_ACCESS_TOKEN'.