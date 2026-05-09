/*!
 * Minimal theme switcher (single-icon toggle)
 *
 * Cycles auto -> light -> dark on click.
 * Persists choice to localStorage; respects system preference in auto.
 */

const themeSwitcher = {
  _scheme: "auto",
  buttonTarget: "[data-theme-switcher-toggle]",
  rootAttribute: "data-theme",
  schemeAttribute: "data-theme-scheme",
  localStorageKey: "picoPreferredColorScheme",
  order: ["auto", "light", "dark"],

  init() {
    this._scheme = this.schemeFromLocalStorage;
    this.applyScheme();
    this.bindButton();
    window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", () => {
      if (this._scheme === "auto") this.applyScheme();
    });
  },

  get schemeFromLocalStorage() {
    const stored = window.localStorage?.getItem(this.localStorageKey);
    return this.order.includes(stored) ? stored : "auto";
  },

  get resolvedScheme() {
    if (this._scheme !== "auto") return this._scheme;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  },

  bindButton() {
    const button = document.querySelector(this.buttonTarget);
    if (!button) return;
    button.addEventListener("click", (event) => {
      event.preventDefault();
      const next = (this.order.indexOf(this._scheme) + 1) % this.order.length;
      this._scheme = this.order[next];
      window.localStorage?.setItem(this.localStorageKey, this._scheme);
      this.applyScheme();
    });
  },

  applyScheme() {
    const html = document.querySelector("html");
    if (!html) return;
    html.setAttribute(this.rootAttribute, this.resolvedScheme);
    html.setAttribute(this.schemeAttribute, this._scheme);
    const button = document.querySelector(this.buttonTarget);
    if (button) {
      const labels = { auto: "Auto theme", light: "Light theme", dark: "Dark theme" };
      button.setAttribute("aria-label", `${labels[this._scheme]} (click to change)`);
      button.setAttribute("title", labels[this._scheme]);
    }
  },
};

themeSwitcher.init();
