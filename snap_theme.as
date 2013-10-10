// HACK:  lazily set theme instance to current theme.
// usage:  in function layer:
// #include "snap_theme.as"
if (this != null && this.root != null) {
    (this.root as MovieClip).snap_theme(this);
}
