# DAVE_requirements

This is non-functional repository with the same requirements as DAVE and its extension modules.

It is used to track the requirements of DAVE and its extension modules.

The requirements are stored in the `requirements.txt` file and can be installed using the following command:

```cmd
pip install -r requirements.txt
```

It is also used to generate the attributions for the DAVE and its extension modules.

```cmd
pip-licenses --with-notice-file --with-license-file --output-file ThirdPartyNotices.html --format html --no-license-path
```

`wcwidth, tomli, prettytable, pip-licenses` are used to generate the attributions and are not part of the requirements.

## automated checks

- Dependabot
- Snyk
