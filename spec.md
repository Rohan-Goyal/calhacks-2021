# Inputs
CSV based on data from a webform.
Each row reps a student, and each col represents a particular attribute.
For the moment, each row represents a
# Outputs
A set of study groups, each with a compatibility score. Each group is a key-value pair of a time (ISO string, I guess?) and a list of students (probably use email ID as unique key).
# Processing
- Filter out groups that don't work based on the time.
- Out of the remaining candidate groups, prune based on heuristics ideally
- Pass through a serious of filters based on compatibility. Each layer should remove the worst candidates, so that successive filters have smaller inputs and we don't take too much time.
- Return an as-exhaustive-as-possible list of groups that fits people into groups based on their preferences and schedules.
# Feature Set
- Webform input
- Students can somehow know which group their in
- We get birds-eye view of every group and all their members.
- Algorithm tries to group people who have similar attrs, like location, experience, priorities/focus area, etc.

# Object Structure/Map
# Random Stuff
IDEA: Each attr has a similarity score. Or use dispatching or whatever, but basically we can compute similarity along various axes and use the mean of that to compute overall similarity.
For instance, specific logic/func to calculate how close two locations are and normalise that somehow.
