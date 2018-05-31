// create an annoymous function to call on showProjectDataForState
// prevents function from showing up globally
// don't want to override variables on accident
(function () {
  //dictionary of states with projects and their details
  window.state_project_map = {};
  // creates helper object in namespace to be referenced in other functions
  window.HELPERS = window.HELPERS || {};

  // function used to display project info on page
  function showProjectDataForState(state) {

    // sets variable to projects of a given state
    const projects = state_project_map[state];

    // queries DOM and obtains projectdata element
    // binds that data to a variable used to display elements
    const projectDisplayEl = document.querySelector('.projectData');

    let projectDisplayElInnerHtml = '';

    // for each project in a list of projects of a given state
    for (let project of projects) {

      // sets inner html to display the project's title using jquery
      projectDisplayElInnerHtml += `<h2>Project: ${project.title}</h2>`;

      // for each property of a project (e.g. title, agency, etc.)
      for (let property in project) {
        projectDisplayElInnerHtml += '<div>' + property + ': ' + project[property] + '</div>';
      }

      // add twitter button with custom text to include project details
      projectDisplayElInnerHtml += '<a class="twitter-share-button" href="https://twitter.com/intent/tweet?text=' + '@' + project.agency + ' , ' + 'EIS ID:' + project.eis_id + '"> Tweet</a>';

      //projectDisplayElInnerHtml += '<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-text="my custom text"' +
      // ' data-show-count="false">Tweet</a>'
      projectDisplayElInnerHtml += ' ' + '<a class="fb-share-button" data-href="https://developers.facebook.com/docs/plugins/" data-layout="button" data-size="small" data-mobile-iframe="true"><a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fplugins%2F&amp;src=sdkpreparse" class="fb-xfbml-parse-ignore">Share</a></a>';

    }

    projectDisplayEl.innerHTML = projectDisplayElInnerHtml;
  }

  window.HELPERS.showProjectDataForState = showProjectDataForState;
})()