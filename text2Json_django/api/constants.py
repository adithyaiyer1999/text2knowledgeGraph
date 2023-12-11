THRESHOLD_FOR_ITERATIVE_UPDATE=400000  #This variable states that if the length of characters is less this then we will call normal create graph function,
                                     #if the length of characters is greater than this then will call multithreading iterative update function
MAX_TOKEN_LENGTH=80000 # Max token length we are permitting for chunking a big paragraph
NUMBER_OF_WORKERS=5 # Number of threads you want to create for launching multithreading setup for calling open ai apis in parallel

# Cachine some of these for the demo

YOUTUBE_CACHE_HTML ='''
<!DOCTYPE html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Inconsolata:wght@300&family=Oswald&display=swap"
rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@1,300&display=swap"
rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inconsolata&display=swap" rel="stylesheet">


<!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>



<style>
ul, #myUL {
    list-style-type: none;
}
li {
    padding-top: 5px;padding-bottom: 5px;
}
#myUL {
    margin: 0;
    padding: 0;
}
.caret {
    cursor: pointer;
    user-select: none;
    font-family: 'Inconsolata', monospace;
}
.caret::before {
    content: " \25B6";
    display: inline-block;
margin-right: 6px;
}
.caret-down::before {
    transform: rotate(90deg); 
}
.nested {
    display: none;
}
.active {
    display: block;
}
.header {
    text-align: left;
    background: #f1f1f1;
}
.text-c {
    color:green;
    font-family:'Inconsolata',monospace;
}
.text-h {
    font-family:'Inconsolata',monospace;
}
</style>


</head>

<body>
<nav class="navbar sticky-top navbar-light bg-light">
        <a class="navbar-brand" href="#">
            <img src="./images/knowledgegraph.png" width="80" height="30" class="d-inline-block align-top" alt=""> JSON2tree
        </a>
    </nav>

<ul class ="myUL"> 
<li><span class="caret">Summary</span> 
<ul class ="nested">
<li><span class="caret">Elon Musk : </span>
  <ul class ="nested">
  <li><span class="caret">Conversations : </span>
    <ul class ="nested">
    <li><span class="caret">On Lex Fridman Podcast : </span>
      <ul class ="nested">
   <li><span class="text-h">Frequency : </span><span class="text-c">Fourth time</span></li>
      <li><span class="caret">Topics Discussed : </span>
        <ul class ="nested">
        <li><span class="caret">Roman Empire : </span>
          <ul class ="nested">
     <li><span class="text-h">Trigger : </span><span class="text-c">Elon's thoughts</span></li>
     <li><span class="text-h">Relation to Today : </span><span class="text-c">Comparison with modern wars and empire dynamics</span></li>
          </ul>
        </li>
        <li><span class="caret">Human Nature and War : </span>
          <ul class ="nested">
     <li><span class="text-h">Question of War : </span><span class="text-c">Part of human nature vs. societal structure consequence</span></li>
     <li><span class="text-h">Elon's View : </span><span class="text-c">Proponent of peace, sees ignorance as the real enemy</span></li>
     <li><span class="text-h">Nature : </span><span class="text-c">View on violence in nature and among other species</span></li>
          </ul>
        </li>
        <li><span class="caret">Intelligence : </span>
          <ul class ="nested">
     <li><span class="text-h">Control Over Violence : </span><span class="text-c">Comparison with animals and control over instincts</span></li>
     <li><span class="text-h">Development of War : </span><span class="text-c">Historical leaders and relation to intelligence</span></li>
          </ul>
        </li>
        <li><span class="caret">Wars and Politics : </span>
          <ul class ="nested">
     <li><span class="text-h">Wars Today : </span><span class="text-c">Views on the utility and consequences of modern wars</span></li>
          <li><span class="caret">Path to Peace : </span>
            <ul class ="nested">
      <li><span class="text-h">Israel and Gaza Conflict : </span><span class="text-c">Complexity and proposed path</span></li>
      <li><span class="text-h">Ukraine War : </span><span class="text-c">Current situation and sensible resolutions</span></li>
      <li><span class="text-h">US-China Tensions : </span><span class="text-c">Discussion on the potential path to avoiding conflict</span></li>
            </ul>
          </li>
          </ul>
        </li>
        <li><span class="caret">Grok AI : </span>
          <ul class ="nested">
     <li><span class="text-h">Development : </span><span class="text-c">Challenges and goals in building AI that understands universe</span></li>
     <li><span class="text-h">Modes : </span><span class="text-c">Existence of fun mode and its significance</span></li>
     <li><span class="text-h">Potential : </span><span class="text-c">To make scientific & theoretical physics discoveries</span></li>
          </ul>
        </li>
        </ul>
      </li>
      </ul>
    </li>
    </ul>
  </li>
  <li><span class="caret">Views on Empire : </span>
    <ul class ="nested">
  <li><span class="text-h">Conquest : </span><span class="text-c">Fundamental engine for many empires</span></li>
  <li><span class="text-h">Roman Empire : </span><span class="text-c">Militaristic and conquest-driven culture</span></li>
    </ul>
  </li>
  <li><span class="caret">Tweet Controversy : </span>
    <ul class ="nested">
    <li><span class="caret">Funding Secured : </span>
      <ul class ="nested">
   <li><span class="text-h">Legal Outcome : </span><span class="text-c">Court found Elon not guilty</span></li>
   <li><span class="text-h">Media Representation : </span><span class="text-c">Misrepresentation compared to court's finding</span></li>
      </ul>
    </li>
    </ul>
  </li>
  <li><span class="caret">Conflict : </span>
    <ul class ="nested">
    <li><span class="caret">With Larry Page : </span>
      <ul class ="nested">
   <li><span class="text-h">Cause : </span><span class="text-c">Creation and direction of OpenAI</span></li>
   <li><span class="text-h">Elon's Stance on AI : </span><span class="text-c">Concern about AI safety and proper regulation</span></li>
      </ul>
    </li>
    </ul>
  </li>
  <li><span class="caret">X Platform : </span>
    <ul class ="nested">
  <li><span class="text-h">Since Acquisition : </span><span class="text-c">Changes and observed improvements</span></li>
  <li><span class="text-h">Recommendation Algorithm : </span><span class="text-c">Efficiency and objectivity goals</span></li>
  <li><span class="text-h">Community Notes : </span><span class="text-c">Success in providing context and notes</span></li>
  <li><span class="text-h">Political Presence and Goals : </span><span class="text-c">Aim for neutrality and free speech support</span></li>
    </ul>
  </li>
  <li><span class="caret">AI Development : </span>
    <ul class ="nested">
  <li><span class="text-h">Autopilot : </span><span class="text-c">End-to-end learning and parallels with human neural net</span></li>
  <li><span class="text-h">Optimus Robot : </span><span class="text-c">Challenges in developing humanoid robot parts</span></li>
    </ul>
  </li>
  <li><span class="caret">Philosophy : </span>
    <ul class ="nested">
  <li><span class="text-h">On War : </span><span class="text-c">Necessity for some degree of conflict for progress</span></li>
  <li><span class="text-h">On Forgiveness : </span><span class="text-c">Focus on future impact rather than holding grudges</span></li>
  <li><span class="text-h">On His Children : </span><span class="text-c">Shared neural net learning insights</span></li>
  <li><span class="text-h">Fundamental Rule : </span><span class="text-c">Only constrained by laws of physics</span></li>
    </ul>
  </li>
  </ul>
</li>
</ul>
</li></ul> 


<script>
var toggler = document.getElementsByClassName("caret");
var i;
for (i = 0; i < toggler.length; i++) {
    toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
}
)}
</script>


</body>
</html>
'''

LLAMA_2_CACHE_HTML ='''
<!DOCTYPE html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Inconsolata:wght@300&family=Oswald&display=swap"
rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@1,300&display=swap"
rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inconsolata&display=swap" rel="stylesheet">


<!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>



<style>
ul, #myUL {
    list-style-type: none;
}
li {
    padding-top: 5px;padding-bottom: 5px;
}
#myUL {
    margin: 0;
    padding: 0;
}
.caret {
    cursor: pointer;
    user-select: none;
    font-family: 'Inconsolata', monospace;
}
.caret::before {
    content: " \25B6";
    display: inline-block;
margin-right: 6px;
}
.caret-down::before {
    transform: rotate(90deg); 
}
.nested {
    display: none;
}
.active {
    display: block;
}
.header {
    text-align: left;
    background: #f1f1f1;
}
.text-c {
    color:green;
    font-family:'Inconsolata',monospace;
}
.text-h {
    font-family:'Inconsolata',monospace;
}
</style>


</head>

<body>
<nav class="navbar sticky-top navbar-light bg-light">
        <a class="navbar-brand" href="#">
            <img src="./images/knowledgegraph.png" width="80" height="30" class="d-inline-block align-top" alt=""> JSON2tree
        </a>
    </nav>

<ul class ="myUL"> 
<li><span class="caret">Summary</span> 
<ul class ="nested">
<li><span class="caret">Model Details : </span>
  <ul class ="nested">
 <li><span class="text-h">Model Developers : </span><span class="text-c">Meta AI</span></li>
  <li><span class="caret">Variations : </span>
    <ul class ="nested">
  <li><span class="text-h">Description : </span><span class="text-c">Llama 2 comes in a range of parameter sizes—7B, 13B, and 70B—as well as pretrained and fine-tuned variations.</span></li>
  <li><span class="text-h">Input : </span><span class="text-c">Models input text only.</span></li>
  <li><span class="text-h">Output : </span><span class="text-c">Models generate text only.</span></li>
    <li><span class="caret">Architecture : </span>
      <ul class ="nested">
   <li><span class="text-h">Type : </span><span class="text-c">Llama 2 is an auto-regressive language model that uses an optimized transformer architecture.</span></li>
   <li><span class="text-h">Alignment : </span><span class="text-c">The tuned versions use supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align to human preferences for helpfulness and safety.</span></li>
      </ul>
    </li>
  <li><span class="text-h">Model Dates : </span><span class="text-c">Llama 2 was trained between January 2023 and July 2023.</span></li>
  <li><span class="text-h">Status : </span><span class="text-c">This is a static model trained on an offline dataset. Future versions of the tuned models will be released as we improve model safety with community feedback.</span></li>
  <li><span class="text-h">License : </span><span class="text-c">A custom commercial license is available at: ai.meta.com/resources/models-and-libraries/llama-downloads/</span></li>
  <li><span class="text-h">Feedback : </span><span class="text-c">Instructions on how to provide feedback or comments on the model can be found in the model README, or by opening an issue in the GitHub repository (https://github.com/facebookresearch/llama/).</span></li>
    </ul>
  </li>
  <li><span class="caret">Intended Use : </span>
    <ul class ="nested">
  <li><span class="text-h">Use Cases : </span><span class="text-c">Llama 2 is intended for commercial and research use in English. Tuned models are intended for assistant-like chat, whereas pretrained models can be adapted for a variety of natural language generation tasks.</span></li>
  <li><span class="text-h">Out-of-Scope Uses : </span><span class="text-c">Use in any manner that violates applicable laws or regulations (including trade compliance laws). Use in languages other than English. Use in any other way that is prohibited by the Acceptable Use Policy and Licensing Agreement for Llama 2.</span></li>
    </ul>
  </li>
  <li><span class="caret">Hardware and Software : </span>
    <ul class ="nested">
  <li><span class="text-h">Training Hardware : </span><span class="text-c">We used custom training libraries, Meta's Research SuperCluster, and production clusters for pretraining. Fine-tuning, annotation, and evaluation were also performed on third-party cloud compute.</span></li>
  <li><span class="text-h">Carbon Footprint : </span><span class="text-c">Pretraining utilized a cumulative 3.3M GPU hours of computation on hardware of type A100-80GB (TDP of 350-400W). Estimated total emissions were 539 tCO2eq, 100% of which were offset by Meta's sustainability program.</span></li>
    </ul>
  </li>
  <li><span class="caret">Training Data : </span>
    <ul class ="nested">
  <li><span class="text-h">Overview : </span><span class="text-c">Llama 2 was pretrained on 2 trillion tokens of data from publicly available sources. The fine-tuning data includes publicly available instruction datasets, as well as over one million new human-annotated examples. Neither the pretraining nor the fine-tuning datasets include Meta user data.</span></li>
  <li><span class="text-h">Data Freshness : </span><span class="text-c">The pretraining data has a cutoff of September 2022, but some tuning data is more recent, up to July 2023.</span></li>
    </ul>
  </li>
 <li><span class="text-h">Evaluation Results : </span><span class="text-c">See evaluations for pretraining (Section 2); fine-tuning (Section 3); and safety (Section 4).</span></li>
  <li><span class="caret">Ethical Considerations and Limitations : </span>
    <ul class ="nested">
  <li><span class="text-h">Description : </span><span class="text-c">Llama 2 is a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Llama 2's potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate or objectionable responses to user prompts. Therefore, before deploying any applications of Llama 2, developers should perform safety testing and tuning tailored to their specific applications of the model. Please see the Responsible Use Guide available at https://ai.meta.com/llama/responsible-user-guide</span></li>
    </ul>
  </li>
  </ul>
</li>
</ul>
</li></ul> 


<script>
var toggler = document.getElementsByClassName("caret");
var i;
for (i = 0; i < toggler.length; i++) {
    toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
}
)}
</script>


</body>
</html>
'''

LLAMA_2_SEARCH_HTML ='''
HERE IT GOES
'''

HARRY_POTTER_HTML ='''
HERE IT GOES
'''
