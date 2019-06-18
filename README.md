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

##### System service APIs
- [x] AdHoc Task Manager Service            :white_check_mark:
- [x] AdHoc Task Progress Reporter          :white_check_mark:
- [x] Admin Data Views Service              :white_check_mark:
- [x] Admin Login Service                   :white_check_mark:
- [x] Admin ObjectLink Builder Service      :white_check_mark:
- [x] Admin Permissions Service             :white_check_mark:
- [x] Applications Service                  :white_check_mark:
- [x] Asset Manager Service                 :white_check_mark:
- [x] Asset Renderer Service                :white_check_mark:
- [x] Asset transformer                     :white_check_mark:
- [x] Audit Service                         :white_check_mark:
- [x] DataManagerCustomizationService       :white_check_mark:
- [x] DataManagerService                    :white_check_mark:
- [x] EmailLayoutService                    :white_check_mark:
- [x] EmailLoggingService                   :white_check_mark:
- [x] EmailMassSendingService               :white_check_mark:
- [x] Email Recipient Type Service          :white_check_mark:
- [x] EmailSendingContextService            :white_check_mark:
- [x] Email service                         :white_check_mark:
- [x] EmailServiceProviderService           :white_check_mark:
- [x] EmailStyleInliner                     :white_check_mark:
- [x] EmailTemplateService                  :white_check_mark:
- [x] Error Log Service                     :white_check_mark:
- [x] Feature service                       :white_check_mark:
- [x] FormBuilderActionsService             :white_check_mark:
- [x] FormBuilderItemTypesService           :white_check_mark:
- [x] FormBuilderRenderingService           :white_check_mark:
- [x] FormBuilderService                    :white_check_mark:
- [x] FormBuilderValidationService          :white_check_mark:
- [x] FormDefinition                        :white_check_mark:
- [x] Forms service                         :white_check_mark:
- [x] HealthcheckService                    :white_check_mark:
- [x] Native Image Manipulation Service     :white_check_mark:
- [x] Notification Service                  :white_check_mark:
- [x] PresideObjectCloningService           :white_check_mark:
- [x] Preside Object Service                :white_check_mark:
- [x] Preside Object View Service           :white_check_mark:
- [x] PresideRestConfigurationWrapper       :white_check_mark:
- [x] Preside REST Request                  :white_check_mark:
- [x] Preside REST Resource Reader          :white_check_mark:
- [x] Preside REST Response                 :white_check_mark:
- [x] Preside Super Class                   :white_check_mark:
- [x] RulesEngine Condition Service         :white_check_mark:
- [x] RulesEngine Context Service           :white_check_mark:
- [x] RulesEngine Expression Reader Service :white_check_mark:
- [x] RulesEngine Expression Service        :white_check_mark:
- [x] RulesEngine Field Type Service        :white_check_mark:
- [x] Rules Engine Filter Service           :white_check_mark:
- [x] RulesEngine Operator Service          :white_check_mark:
- [x] RulesEngine Time Period Service       :white_check_mark:
- [x] RulesEngine Web Request Service       :white_check_mark:
- [x] SimpleColourPickerService             :white_check_mark:
- [x] Storage provider                      :white_check_mark:
- [x] System configuration service          :white_check_mark:
- [x] SystemEmailTemplateService            :white_check_mark:
- [x] TaskManager Configuration Wrapper     :white_check_mark:
- [x] Task Manager Service                  :white_check_mark:
- [x] ThreadUtil                            :white_check_mark:
- [x] Validation Engine                     :white_check_mark:
- [x] Validation result                     :white_check_mark:
- [x] ViewletsService                       :white_check_mark:
- [x] Website login service                 :white_check_mark:
- [x] Website permissions service           :white_check_mark:
- [x] Website user action service           :white_check_mark:
- [x] Website user impersonation service    :white_check_mark:
- [x] Website visitor service               :white_check_mark:

### AdHocTaskManagerService
<details>
	<summary>List of functions</summary>

	- `completeTask()`
	- `createTask()`
	- `discardTask()`
	- `failTask()`
	- `getNextAttemptInfo()`
	- `getNextScheduledTaskToRun()`
	- `getProgress()`
	- `getTask()`
	- `markTaskAsRunning()`
	- `requeueTask()`
	- `runScheduledTasks()`
	- `runTask()`
	- `runTaskInThread()`
	- `setProgress()`
	- `setResult()`
	- `setResultUrl()`
</details>