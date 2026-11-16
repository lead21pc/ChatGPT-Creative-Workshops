# HUB-IMAGET-ENTRY

Module ID: HUB-IMAGET-ENTRY
Package ID: HUB-PKG-IMAGET
Runtime role: TOOL_PIPELINE
Scope: ImageT binding and scoped handoff
Status: ACTIVE
Version: 1.5

After Hub selection, use the Hub Router Library contract to resolve the following ACTIVE objects in HUB-PKG-IMAGET, role DOMAIN_PROCEDURE. The filenames are install artifacts in ImageT/, not locators.

| Module ID | Version | Required |
| --- | --- | --- |
| HUB-IMAGET-CORE-CONTROLLER | 1.5 | All ImageT operations |
| HUB-IMAGET-AD-ANTI-PRIOR | 1.4.0 | All ImageT operations |
| HUB-IMAGET-CORE-READY-GATE | 1.3 | CREATE, EDIT, VARIATION, CORRECT and each generation retry |

Return actual reads and blockers to Hub. Delegate operation, authority, optional selection and prompt work to Controller with the root-declared local Catalog binding. ANALYZE needs no Ready Gate. Every generation must pass Prompt Gate then Ready Gate before a tool send. Unresolved required objects block dependent work.
