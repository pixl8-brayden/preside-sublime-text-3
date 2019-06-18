# Sublime Text Preside Package
Sublime Text Preside Package is a collection of Preside snippets and auto completions for Sublime Text 3

Preside full documentation refer link
[Preside Documentation](https://docs.preside.org)

## Features
Autocomplete for:

Up to Preside version: `10.10.67`

## Notes

## CFML Tags
| Tags              | Output                       |
|-------------------|------------------------------|
| `cfpresideparam`  | <cf_presideparam name="paramName" editable="true" /> |
| `cfelse`          | <cfelse>                                             |
| `cfif`            | <cfif statement>...</cfif>                           |
| `cfifelse`        | <cfif statement>...<cfelse>...</cfif>                |
| `cfloop`          | <cfloop statement>...</cfloop>                       |
| `cfoutput`        | <cfoutput>...</cfoutput>                             |
| `cfparam`         | <cfparam name="name" />                              |
| `cfscript`        | <cfscript>...</cfscript>                             |
| `cfset`           | <cfset variable = value />                           |
| `cfswitch`        | <cfswitch>...</cfswitch>                             |
| `cfwhile`         | <cfwhile condition>...</cfwhile>                     |

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

##### System service APIs
- [x] AdHoc Task Manager Service         :white_check_mark:
- [x] AdHoc Task Progress Reporter       :white_check_mark:
- [x] Admin Data Views Service           :white_check_mark:
- [x] Admin Login Service                :white_check_mark:
- [x] Admin ObjectLink Builder Service   :white_check_mark:
- [x] Admin Permissions Service          :white_check_mark:
- [ ] Applications Service
- [x] Asset Manager Service              :white_check_mark:
- [x] Asset Renderer Service             :white_check_mark:
- [x] Asset transformer                  :white_check_mark:
- [ ] Audit Service
- [ ] Database Migration Service
- [ ] DataExporterReader
- [ ] DataExportService
- [ ] DataManagerCustomizationService
- [ ] DataManagerService
- [ ] DelayedStickerRendererService
- [ ] DelayedViewletRendererService
- [x] EmailLayoutService                 :white_check_mark:
- [x] EmailLoggingService                :white_check_mark:
- [x] EmailMassSendingService            :white_check_mark:
- [x] Email Recipient Type Service       :white_check_mark:
- [x] EmailSendingContextService         :white_check_mark:
- [x] Email service                      :white_check_mark:
- [x] EmailServiceProviderService        :white_check_mark:
- [x] EmailStyleInliner                  :white_check_mark:
- [x] EmailTemplateService               :white_check_mark:
- [ ] Error Log Service
- [ ] Feature service
- [ ] File System Storage Provider
- [x] FormBuilderActionsService          :white_check_mark:
- [x] FormBuilderItemTypesService        :white_check_mark:
- [x] FormBuilderRenderingService        :white_check_mark:
- [x] FormBuilderService                 :white_check_mark:
- [x] FormBuilderValidationService       :white_check_mark:
- [x] FormDefinition                     :white_check_mark:
- [x] Forms service                      :white_check_mark:
- [ ] HealthcheckService
- [ ] Multilingual Preside Object Service
- [ ] Native Image Manipulation Service
- [x] Notification Service               :white_check_mark:
- [ ] PresideObjectCloningService
- [x] Preside Object Service             :white_check_mark:
- [x] Preside Object View Service        :white_check_mark:
- [x] PresideRestConfigurationWrapper    :white_check_mark:
- [x] Preside REST Request               :white_check_mark:
- [x] Preside REST Resource Reader       :white_check_mark:
- [x] Preside REST Response              :white_check_mark:
- [x] Preside Super Class                :white_check_mark:
- [ ] RulesEngine Condition Service
- [ ] RulesEngine Context Service
- [ ] RulesEngine Expression Reader Service
- [ ] RulesEngine Expression Service
- [ ] RulesEngine Field Type Service
- [ ] Rules Engine Filter Service
- [ ] RulesEngine Operator Service
- [ ] RulesEngine Time Period Service
- [ ] RulesEngine Web Request Service
- [ ] SimpleColourPickerService
- [ ] Storage provider
- [ ] System configuration service
- [ ] SystemEmailTemplateService
- [ ] TaskManager Configuration Wrapper
- [ ] TaskManager Logger Wrapper
- [ ] Task Manager Service
- [ ] ThreadUtil
- [ ] Validation Engine
- [ ] Validation result
- [x] ViewletsService                    :white_check_mark:
- [x] Website login service              :white_check_mark:
- [x] Website permissions service        :white_check_mark:
- [x] Website user action service        :white_check_mark:
- [x] Website user impersonation service :white_check_mark:
- [x] Website visitor service            :white_check_mark:

##### System Form Controls :white_check_mark:

##### CSRF Protection      :white_check_mark:
| Available Functions | Return Type |
|---------------------|-------------|
| `getCsrfToken`      | n/a         |
| `validateCsrfToken` | boolean     |
