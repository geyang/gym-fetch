from cmx import doc

doc @ """
# Extended Taskset for the Fetch Robot

## Lsit of environments

Existing Fetch environments from gym
"""
doc.csv @ """
Name,           Progress,  ID
Reach-v2,       ✅ gym,     
Push-v2,        ✅ gym,     
PickPlace-v2,   ✅ gym,      
Slide-v2,       ✅ gym,      
"""

doc @ """
New environments we want to build
"""
doc.csv @ """
Name,           Progress,  ID
Bin-picking-v2,     ,      
Box-open-v2,        ,      
Box-close-v2,       ,      
"""

doc.flush()