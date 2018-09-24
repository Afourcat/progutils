# progutils
Little python script where you can easily add your modules.

## Concept
Here the concept is not the code but the idea of a module added by the community
in the folder `modules` you can add your own folder with the config file inside.
Your module can use executable linked to a name inside the config file.

Example:
```
modules |
        `-base -.
        |       | mod.toml
        |       | test.sh
        |       | linter
        |       `
        |
        `-ident-.
        |       | mod.toml
        |       | to_tabs
        |       | to_spaces
        |
        `-  my -.
        |       | mod.toml
        |       | my_linter
        |       | my_nice_script
        |
        `- java-.
                | mod.toml
                | javadoc
                | tester.x
```

A mod.toml example
```
name="java"

description="A nice module for java dependent of `my` module"

[commands]
doc="javadoc"
linter="../my/my_linter"
test="tester.x"
```
