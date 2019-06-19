# Sublime Text Preside Package
Sublime Text Preside Package is a collection of Preside snippets and auto completions for Sublime Text 3

Preside full documentation refer link
[Preside Documentation](https://docs.preside.org)

## Features
Autocomplete for:

Up to Preside version: `10.10.76`

## Notes

## CFML Tags
| Triggers          | Output                       |
|-------------------|------------------------------|
| `cfpresideparam`  | `<cf_presideparam name="..." editable="true" />` |
| `cfelse`          | `<cfelse>`                                       |
| `cfif`            | `<cfif statement>...</cfif>`                     |
| `cfifelse`        | `<cfif statement>...<cfelse>...</cfif>`          |
| `cfloop`          | `<cfloop statement>...</cfloop>`                 |
| `cfoutput`        | `<cfoutput>...</cfoutput>`                       |
| `cfparam`         | `<cfparam name = "..." /> `                      |
| `cfscript`        | `<cfscript>...</cfscript>`                       |
| `cfset`           | `<cfset variable = value /> `                    |
| `cfswitch`        | `<cfswitch>...</cfswitch>`                       |
| `cfwhile`         | `<cfwhile condition>...</cfwhile>`               |

## Snippets
| Snippets          | Description                  |
|-------------------|------------------------------|
| `form`            | Generate base for Preside Form XML |
| `dataObject`      | Generate base for Preside Object Component |
| `superclass`      | Generate base for Preside Object Component with super class applied |
| `publicfunction`  | Generate base for public function |
| `privatefunction` | Generate base for private function |

## Functions
[ Included : :white_check_mark: ]

##### System Form Controls :white_check_mark:

##### CSRF Protection      :white_check_mark:
| Available Functions | Return Type |
|---------------------|-------------|
| `getCsrfToken`      | n/a         |
| `validateCsrfToken` | boolean     |
