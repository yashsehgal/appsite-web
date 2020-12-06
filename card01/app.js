var component = document.createElement("component");
component.innerHTML = `
<div id="component-container">
  <div id="component-screenshot">
    <p id="watch-online">Watch Online ></p>
    </div>
    <div id="flex-handler">
    <div id="component-description">
    <p id="component-title-heading" class="componentTitleHeading">
      Modern. Simple. Header Component
      </p>
      <p id="user-description" class="user-desc">
      By, John Doe
      </p>
     
      <div id="component-usage-buttons">
        <div id="link-margin-handler">
          <a href="#" id="getCodeLink">Copy HTML</a>
          <a href="#" id="getCodeLink">Copy CSS</a>
        </div>
        <img src="downloadButton01.svg" alt="download" id="downloadCodeButton">
      </div>
     
      <p id="languages-used">HTML, CSS</p>
    </div>
    </div>
  </div>
`;

document.getElementById("container").appendChild(component);