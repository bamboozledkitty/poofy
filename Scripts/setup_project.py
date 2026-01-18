import os
import re

PROJECT_PATH = "Poofy.xcodeproj/project.pbxproj"
SCHEME_DIR = "Poofy.xcodeproj/xcshareddata/xcschemes"
SCHEME_PATH = f"{SCHEME_DIR}/Poofy.xcscheme"

# IDs
GPX_FILE_ID = "B13C99912CE7CD0F00D6B4D5"
SCRIPT_PHASE_ID = "B13C99922CE7CD0F00D6B4D5"
TARGET_ID = "B13C90B82CE7CD0F00D6B4D5"
MAIN_GROUP_ID = "B13C90B02CE7CD0F00D6B4D5"

def modify_project_file():
    with open(PROJECT_PATH, 'r') as f:
        content = f.read()

    # 1. Add PBXFileReference for GPX file if missing
    if "SimulatedLocation.gpx" not in content:
        print("Adding GPX File Reference...")
        file_ref = f'\t\t{GPX_FILE_ID} /* SimulatedLocation.gpx */ = {{isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.xml; name = SimulatedLocation.gpx; path = Poofy/SimulatedLocation.gpx; sourceTree = "<group>"; }};\n'
        
        # Insert into PBXFileReference section
        content = re.sub(r'(/\* Begin PBXFileReference section \*/\n)', f'\\1{file_ref}', content)
        
        # Add to Main Group
        # Find the children list of the main group
        group_match = re.search(r'(' + MAIN_GROUP_ID + r' = \{.*?children = \()(.*?)(\);)', content, re.DOTALL)
        if group_match:
            # Add to the beginning of children
            new_children = f'\n\t\t\t\t{GPX_FILE_ID} /* SimulatedLocation.gpx */,{group_match.group(2)}'
            content = content.replace(group_match.group(0), f'{group_match.group(1)}{new_children}{group_match.group(3)}')

    # 2. Add Run Script Phase if missing
    if "generate_gpx.sh" not in content:
        print("Adding Shell Script Phase...")
        script_phase = f'''
/* Begin PBXShellScriptBuildPhase section */
\t\t{SCRIPT_PHASE_ID} /* ShellScript */ = {{
\t\t\tisa = PBXShellScriptBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t);
\t\t\tinputFileListPaths = (
\t\t\t);
\t\t\tinputPaths = (
\t\t\t);
\t\t\toutputFileListPaths = (
\t\t\t);
\t\t\toutputPaths = (
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t\tshellPath = /bin/sh;
\t\t\tshellScript = "\\"${{PROJECT_DIR}}/Scripts/generate_gpx.sh\\"";
\t\t}};
/* End PBXShellScriptBuildPhase section */
'''
        # Insert section (e.g. before PBXSourcesBuildPhase)
        content = re.sub(r'(/\* Begin PBXSourcesBuildPhase)', f'{script_phase}\\1', content)

        # Add to Target Build Phases
        # We want to run this BEFORE compiling sources, ideally.
        target_match = re.search(r'(' + TARGET_ID + r' /\* Poofy \*/ = \{.*?buildPhases = \()(.*?)(\);)', content, re.DOTALL)
        if target_match:
            # Insert at the top of buildPhases
            new_phases = f'\n\t\t\t\t{SCRIPT_PHASE_ID} /* ShellScript */,{target_match.group(2)}'
            content = content.replace(target_match.group(0), f'{target_match.group(1)}{new_phases}{target_match.group(3)}')

    with open(PROJECT_PATH, 'w') as f:
        f.write(content)
    print("Project file updated.")

def create_shared_scheme():
    if not os.path.exists(SCHEME_DIR):
        os.makedirs(SCHEME_DIR)
    
    # Simple Scheme Template
    # Crucially: allowLocationSimulation = "YES" and LocationScenarioReference pointing to our file
    scheme_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<Scheme
   LastUpgradeVersion = "1610"
   version = "1.7">
   <BuildAction
      parallelizeBuildables = "YES"
      buildImplicitDependencies = "YES">
      <BuildActionEntries>
         <BuildActionEntry
            buildForTesting = "YES"
            buildForRunning = "YES"
            buildForProfiling = "YES"
            buildForArchiving = "YES"
            buildForAnalyzing = "YES">
            <BuildableReference
               BuildableIdentifier = "primary"
               BlueprintIdentifier = "{TARGET_ID}"
               BuildableName = "Poofy.app"
               BlueprintName = "Poofy"
               ReferencedContainer = "container:Poofy.xcodeproj">
            </BuildableReference>
         </BuildActionEntry>
      </BuildActionEntries>
   </BuildAction>
   <TestAction
      buildConfiguration = "Debug"
      selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB"
      selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB"
      shouldUseLaunchSchemeArgsEnv = "YES">
      <Testables>
      </Testables>
   </TestAction>
   <LaunchAction
      buildConfiguration = "Debug"
      selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB"
      selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB"
      launchStyle = "0"
      useCustomWorkingDirectory = "NO"
      ignoresPersistentStateOnLaunch = "NO"
      debugDocumentVersioning = "YES"
      debugServiceExtension = "internal"
      allowLocationSimulation = "YES">
      <LocationScenarioReference
         identifier = "Poofy/SimulatedLocation.gpx"
         referenceType = "0">
      </LocationScenarioReference>
      <BuildableProductRunnable
         runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "{TARGET_ID}"
            BuildableName = "Poofy.app"
            BlueprintName = "Poofy"
            ReferencedContainer = "container:Poofy.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
   </LaunchAction>
   <ProfileAction
      buildConfiguration = "Release"
      shouldUseLaunchSchemeArgsEnv = "YES"
      savedToolIdentifier = ""
      useCustomWorkingDirectory = "NO"
      debugDocumentVersioning = "YES">
      <BuildableProductRunnable
         runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "{TARGET_ID}"
            BuildableName = "Poofy.app"
            BlueprintName = "Poofy"
            ReferencedContainer = "container:Poofy.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
   </ProfileAction>
   <AnalyzeAction
      buildConfiguration = "Debug">
   </AnalyzeAction>
   <ArchiveAction
      buildConfiguration = "Release"
      revealArchiveInOrganizer = "YES">
   </ArchiveAction>
</Scheme>
'''
    with open(SCHEME_PATH, 'w') as f:
        f.write(scheme_content)
    print(f"Created/Updated Shared Scheme at {SCHEME_PATH}")

if __name__ == "__main__":
    modify_project_file()
    create_shared_scheme()
