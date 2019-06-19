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
| Triggers          | Description                  |
|-------------------|------------------------------|
| `form`            | Generate base for Preside Form XML                         |
| `dataObject`      | Generate base for Preside Object Component                 |
| `superclass`      | Generate base for Preside Service with super class applied |
| `publicfunction`  | Generate base for public function                          |
| `privatefunction` | Generate base for private function                         |

## i18n
| Triggers            | Description                  |
|-------------------- |------------------------------|
| `i18nBasic`         | Generate base for basic i18n                |
| `i18nField`         | *Generate field i18n*                       |
| `i18nPageTypes`     | Generate base for page types i18n           |
| `i18nGroup`         | Generate base for preside object group i18n |
| `i18nPresideObject` | Generate base for preside object i18n       |

## CSRF Protection
| Available Functions | Return Type |
|---------------------|-------------|
| `getCsrfToken`      | n/a         |
| `validateCsrfToken` | boolean     |
