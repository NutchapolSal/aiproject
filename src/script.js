/**
 * Expose functions to be used in Python code
 *
 * e.g. `gr.Button().click(fn=None, js="myFunction")`
 */
function initialize() {

  /**
   * @param {string} curPage page to be hidden away
   * @param {string} newPage page to switch in place (be visible)
   */
  globalThis.switchPage = (curPage, newPage) => {
    $("." + curPage).css({
      'visibility': 'hidden',
      'position': 'absolute',
    });
    $("." + newPage).css({
      'visibility': 'visible',
      'position': 'relative',
    })
  }

}