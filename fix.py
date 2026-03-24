import os
f = os.path.join(os.path.dirname(__file__), 'index.html')
with open(f, 'r', encoding='utf-8') as fh:
    lines = fh.readlines()

# Find the line "    </div>" after the close-btn (around line 234-235)
# and remove everything between it and the legendBox div
start_del = None
end_del = None
for i in range(230, min(280, len(lines))):
    line = lines[i].strip()
    # Find first orphaned line after "</div>" closing mainOverlay
    if 'id="layerBeyazKusak"' in lines[i] or 'id="layerDropdown"' in lines[i] or 'id="layerDropBtn"' in lines[i]:
        if start_del is None:
            start_del = i
    if 'id="layerPasifikGuney"' in lines[i] and start_del is not None:
        # Continue to find the end
        pass
    if start_del is not None and ('id="legendBox"' in lines[i] or 'class="legend"' in lines[i]):
        end_del = i
        break

if start_del is None:
    print("No orphaned content found - file may already be clean!")
else:
    if end_del is None:
        # Just find the next legendBox
        for i in range(start_del, len(lines)):
            if 'legendBox' in lines[i]:
                end_del = i
                break
    
    if end_del:
        removed = lines[start_del:end_del]
        new_lines = lines[:start_del] + ['\n'] + lines[end_del:]
        with open(f, 'w', encoding='utf-8') as fh:
            fh.writelines(new_lines)
        print(f"Removed {len(removed)} orphaned lines (lines {start_del+1}-{end_del})")
        print(f"File: {len(lines)} -> {len(new_lines)} lines")
    else:
        print("Could not find end marker (legendBox)")

print("Done! Refresh browser with Ctrl+Shift+R")
