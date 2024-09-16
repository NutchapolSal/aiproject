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
      'visibility': 'inherit',
      'position': 'inherit',
    })
  }

  let initMainMenu = () => {
    console.log("init menu");
  }

  initMainMenu();

  let elementsToAdd = [
    /* Main menu */
    `
      <div class="main-menu">
        <h1 class="title">Welcome to RPS with AI!</h1>
      </div>
    `,
    /* Play */
    `
      <div class="play">
        <h1 class="title">Let's play some game!</h1>
      </div>
    `,
    /* References */
    `
      <div class="references">
        <p>
          Created by
        </p>
      </div>
    `
  ];

  elementsToAdd.forEach(section => {
    $(".gradio-container").prepend(section);
  });
}