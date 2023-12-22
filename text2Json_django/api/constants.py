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
    content: \" \\25B6\";
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
            <img src="./images/knowledgegraph.png" width="80" height="30" class="d-inline-block align-top" alt=""> Your Tree:
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
            content: \" \\25B6\";
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
        <img src="./images/knowledgegraph.png" width="80" height="30" class="d-inline-block align-top" alt=""> Your Tree:
    </a>
</nav>

<ul class ="myUL">
    <li><span class="caret">Summary</span>
        <ul class ="nested">
            <li><span class="caret">Llama 2 : </span>
                <ul class ="nested">
                    <li><span class="text-h">description : </span><span class="text-c">A collection of pretrained and fine-tuned large language models (LLMs)</span></li>
                    <li><span class="text-h">range : </span><span class="text-c">7 billion to 70 billion parameters</span></li>
                    <li><span class="caret">optimization : </span>
                        <ul class ="nested">
                            <li><span class="text-h">use_case : </span><span class="text-c">dialogue</span></li>
                            <li><span class="caret">techniques : [2]</span>
                                <ul class ="nested">
                                    <li><span class="text-c">Supervised Fine-Tuning (SFT)</span>
                                    </li>
                                    <li><span class="text-c">Reinforcement Learning with Human Feedback (RLHF)</span>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <li><span class="caret">performance : </span>
                        <ul class ="nested">
                            <li><span class="text-h">benchmarks : </span><span class="text-c">outperforms open-source chat models on most tests</span></li>
                            <li><span class="caret">human_evaluations : </span>
                                <ul class ="nested">
                                    <li><span class="text-h">helpfulness : </span><span class="text-c">comparable to some closed-source models based on tests</span></li>
                                    <li><span class="text-h">safety : </span><span class="text-c">measures taken to increase safety through data annotation and tuning</span></li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <li><span class="caret">contributions : </span>
                        <ul class ="nested">
                            <li><span class="text-h">see_details : </span><span class="text-c">Section A.1</span></li>
                        </ul>
                    </li>
                    <li><span class="caret">pretraining_methodology : </span>
                        <ul class ="nested">
                            <li><span class="text-h">data : </span><span class="text-c">A mix of publicly available sources, excluding Meta user data</span></li>
                            <li><span class="text-h">training_corpus_size : </span><span class="text-c">2 trillion tokens</span></li>
                            <li><span class="caret">modifications : </span>
                                <ul class ="nested">
                                    <li><span class="text-h">robust_data_cleaning : </span><span class="text-c">None</span></li>
                                    <li><span class="text-h">data_mix_updates : </span><span class="text-c">None</span></li>
                                    <li><span class="text-h">context_length : </span><span class="text-c">doubled</span></li>
                                    <li><span class="text-h">grouped-query_attention : </span><span class="text-c">for larger models</span></li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <li><span class="caret">fine_tuning_methodology : </span>
                        <ul class ="nested">
                            <li><span class="text-h">starting_point : </span><span class="text-c">Publicly available instruction tuning data</span></li>
                            <li><span class="text-h">high_quality_SFT_data_collection : </span><span class="text-c">focus on quality vs quantity</span></li>
                            <li><span class="caret">RLHF : </span>
                                <ul class ="nested">
                                    <li><span class="text-h">human_preference_data_collection : </span><span class="text-c">binary comparison protocol</span></li>
                                    <li><span class="text-h">reward_model_training : </span><span class="text-c">binary ranking loss, margin component</span></li>
                                    <li><span class="caret">iterative_fine_tuning : [2]</span>
                                        <ul class ="nested">
                                            <li><span class="text-c">Rejection Sampling fine-tuning</span>
                                            </li>
                                            <li><span class="text-c">PPO</span>
                                            </li>
                                        </ul>
                                    </li>
                                </ul>
                            </li>
                            <li><span class="caret">multi_turn_consistency : </span>
                                <ul class ="nested">
                                    <li><span class="text-h">technique : </span><span class="text-c">Ghost Attention (GAtt)</span></li>
                                    <li><span class="text-h">evaluation : </span><span class="text-c">consistent up to 20+ turns</span></li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <li><span class="caret">safety_aspect : </span>
                        <ul class ="nested">
                            <li><span class="caret">pretraining_investigations : [3]</span>
                                <ul class ="nested">
                                    <li><span class="text-c">demographic_representation</span>
                                    </li>
                                    <li><span class="text-c">toxicity_measurement</span>
                                    </li>
                                    <li><span class="text-c">language_identification</span>
                                    </li>
                                </ul>
                            </li>
                            <li><span class="caret">fine-tuning_for_safety : </span>
                                <ul class ="nested">
                                    <li><span class="caret">categories_and_annotations : </span>
                                        <ul class ="nested">
                                            <li><span class="caret">risk_categories : [3]</span>
                                                <ul class ="nested">
                                                    <li><span class="text-c">illicit activities</span>
                                                    </li>
                                                    <li><span class="text-c">harmful activities</span>
                                                    </li>
                                                    <li><span class="text-c">unqualified advice</span>
                                                    </li>
                                                </ul>
                                            </li>
                                            <li><span class="caret">attack_vectors : [3]</span>
                                                <ul class ="nested">
                                                    <li><span class="text-c">psychological manipulation</span>
                                                    </li>
                                                    <li><span class="text-c">syntactic manipulation</span>
                                                    </li>
                                                    <li><span class="text-c">semantic manipulation</span>
                                                    </li>
                                                </ul>
                                            </li>
                                            <li><span class="text-h">safety_guidelines : </span><span class="text-c">mitigate risks through supervision and RLHF</span></li>
                                        </ul>
                                    </li>
                                    <li><span class="caret">RLHF_for_safety : </span>
                                        <ul class ="nested">
                                            <li><span class="text-h">annotator_instructions : </span><span class="text-c">prioritize safety over helpfuness if needed</span></li>
                                            <li><span class="text-h">impact : </span><span class="text-c">decreased toxicity, increased truthfulness after fine-tuning</span></li>
                                        </ul>
                                    </li>
                                    <li><span class="text-h">context_distillation : </span><span class="text-c">teaches model to generate safe outputs</span></li>
                                    <li><span class="text-h">red_teaming : </span><span class="text-c">proactive risk identification and mitigation</span></li>
                                </ul>
                            </li>
                            <li><span class="caret">evaluation : </span>
                                <ul class ="nested">
                                    <li><span class="caret">methods : [2]</span>
                                        <ul class ="nested">
                                            <li><span class="text-c">human evaluation</span>
                                            </li>
                                            <li><span class="text-c">automatic safety benchmarks</span>
                                            </li>
                                        </ul>
                                    </li>
                                    <li><span class="caret">results : </span>
                                        <ul class ="nested">
                                            <li><span class="text-h">benchmarks : </span><span class="text-c">improved over open-source models for toxicity and truthfulness</span></li>
                                            <li><span class="text-h">human_evaluation : </span><span class="text-c">low violation percentage and high safety ratings</span></li>
                                        </ul>
                                    </li>
                                </ul>
                            </li>
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
    content: \" \\25B6\";
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
            <img src="./images/knowledgegraph.png" width="80" height="30" class="d-inline-block align-top" alt=""> Your Tree:
        </a>
    </nav>

<ul class ="myUL">
<li><span class="caret">Summary</span>
<ul class ="nested">
<li><span class="caret">Llama 2 : </span>
  <ul class ="nested">
  <li><span class="caret">performance : </span>
    <ul class ="nested">
    <li><span class="caret">benchmarks : </span>
      <ul class ="nested">
   <li><span class="text-h">benchmarks : </span><span class="text-c">outperforms open-source chat models on most tests</span></li>
      <li><span class="caret">human_evaluations : </span>
        <ul class ="nested">
    <li><span class="text-h">helpfulness : </span><span class="text-c">comparable to some closed-source models based on tests</span></li>
    <li><span class="text-h">safety : </span><span class="text-c">measures taken to increase safety through data annotation and tuning</span></li>
        </ul>
      </li>
      </ul>
    </li>
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
...ChatgptResponse...Llama 2's strengths, based on the provided tree, include outperforming open-source chat models on most tests and having a comparable helpfulness to some closed-source models based on tests. Additionally, there are measures taken to increase safety through data annotation and tuning.
'''

HARRY_POTTER_HTML ='''
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
    content: \" \\25B6\";
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
            <img src="./images/knowledgegraph.png" width="80" height="30" class="d-inline-block align-top" alt=""> Your Tree :
        </a>
    </nav>

<ul class ="myUL">
<li><span class="caret">Summary</span>
<ul class ="nested">
<li><span class="caret">The Sorcerer's Stone : </span>
  <ul class ="nested">
  <li><span class="caret">Characters : </span>
    <ul class ="nested">
    <li><span class="caret">Dursleys : </span>
      <ul class ="nested">
   <li><span class="text-h">Description : </span><span class="text-c">Normal family disapproving of anything strange, fearful of their connection to the Potters being exposed</span></li>
      <li><span class="caret">Members : </span>
        <ul class ="nested">
        <li><span class="caret">Mr. Dursley : </span>
          <ul class ="nested">
     <li><span class="text-h">Profession : </span><span class="text-c">Director of a firm called Grunnings</span></li>
     <li><span class="text-h">Physical : </span><span class="text-c">Big, beefy man with hardly any neck, large mustache</span></li>
     <li><span class="text-h">Behavior : </span><span class="text-c">Notices strange events, gets upset at people in cloaks, shocked by the mention of the Potters</span></li>
          </ul>
        </li>
        <li><span class="caret">Mrs. Dursley : </span>
          <ul class ="nested">
     <li><span class="text-h">Physical : </span><span class="text-c">Thin, blonde, nearly twice the usual amount of neck</span></li>
     <li><span class="text-h">Activities : </span><span class="text-c">Spends much time spying on neighbors</span></li>
          </ul>
        </li>
        <li><span class="caret">Dudley : </span>
          <ul class ="nested">
     <li><span class="text-h">Description : </span><span class="text-c">Prized by his parents, no finer boy, anticipation of shared future experience with the narrator</span></li>
     <li><span class="text-h">Birthday : </span><span class="text-c">Receives many presents and attention, an outing to the zoo results in the disappearance of glass from an enclosure</span></li>
          </ul>
        </li>
        </ul>
      </li>
      </ul>
    </li>
    <li><span class="caret">Harry Potter : </span>
      <ul class ="nested">
   <li><span class="text-h">Living Conditions : </span><span class="text-c">Sleeps in a cupboard, poorly treated, birthday neglected</span></li>
      <li><span class="caret">Encounters : </span>
        <ul class ="nested">
    <li><span class="text-h">With the Dursleys : </span><span class="text-c">Left on the doorstep, neglected, punished after zoo incident</span></li>
    <li><span class="text-h">With Voldemort : </span><span class="text-c">Pain from scar, reveals Voldemort's past with parents</span></li>
    <li><span class="text-h">With Centaurs : </span><span class="text-c">Discussed foreboding events, fate of the unicorn</span></li>
    <li><span class="text-h">With Dumbledore : </span><span class="text-c">Discussed the Sorcerer's Stone, received explanations</span></li>
        </ul>
      </li>
      <li><span class="caret">Actions : </span>
        <ul class ="nested">
    <li><span class="text-h">Glass Disappearance Incident : </span><span class="text-c">Unintentionally caused glass to disappear at a zoo's boa constrictor enclosure</span></li>
    <li><span class="text-h">Discovers Mirror of Erised : </span><span class="text-c">Sees his deceased parents, deepest desires revealed</span></li>
    <li><span class="text-h">Learns about Nicolas Flamel : </span><span class="text-c">Identity as alchemist and creator of the Sorcerer's Stone</span></li>
    <li><span class="text-h">Understands Voldemort's Goal : </span><span class="text-c">To use the Stone to regain form and power</span></li>
        </ul>
      </li>
      <li><span class="caret">Feelings : </span>
        <ul class ="nested">
    <li><span class="text-h">About Quidditch and Friendship : </span><span class="text-c">Cherishes moments and values friendships</span></li>
    <li><span class="text-h">About Discoveries : </span><span class="text-c">Overwhelmed by truth of Stone and Voldemort's plans</span></li>
        </ul>
      </li>
      </ul>
    </li>
    <li><span class="caret">Hermione Granger : </span>
      <ul class ="nested">
   <li><span class="text-h">Contributions : </span><span class="text-c">Solves riddles, gathers information about the Stone</span></li>
      </ul>
    </li>
    <li><span class="caret">Ron Weasley : </span>
      <ul class ="nested">
   <li><span class="text-h">Contributions : </span><span class="text-c">Key role in chess game protecting the Stone</span></li>
      </ul>
    </li>
    <li><span class="caret">Professor Quirrell : </span>
      <ul class ="nested">
   <li><span class="text-h">Revelation : </span><span class="text-c">Host for Voldemort, attempts to steal Stone</span></li>
      </ul>
    </li>
    <li><span class="caret">Professor Snape : </span>
      <ul class ="nested">
   <li><span class="text-h">Misconceptions : </span><span class="text-c">Suspected of theft, actually protecting Harry</span></li>
      </ul>
    </li>
    <li><span class="caret">Voldemort : </span>
      <ul class ="nested">
   <li><span class="text-h">Fate : </span><span class="text-c">Weakened but a looming threat seeking to regain power</span></li>
      </ul>
    </li>
    <li><span class="caret">Neville Longbottom : </span>
      <ul class ="nested">
   <li><span class="text-h">Personal Growth : </span><span class="text-c">Stands up for the greater good, earns points for Gryffindor</span></li>
      </ul>
    </li>
    </ul>
  </li>
  <li><span class="caret">Events : </span>
    <ul class ="nested">
    <li><span class="caret">Dursley's Day : </span>
      <ul class ="nested">
   <li><span class="text-h">Morning : </span><span class="text-c">Odd behavior in town, cat reading map, cloaked people</span></li>
   <li><span class="text-h">News : </span><span class="text-c">Unusual owl activity and shooting stars attributed to odd weather or celebrations</span></li>
   <li><span class="text-h">Encounters : </span><span class="text-c">Strangers discussing Potters, violet cloak stranger happy about You-Know-Who's disappearance</span></li>
      </ul>
    </li>
    <li><span class="caret">Evening : </span>
      <ul class ="nested">
   <li><span class="text-h">Arrival of Dumbledore and McGonagall : </span><span class="text-c">Discussion of You-Know-Who, Potter's fate, leaving of baby Harry</span></li>
   <li><span class="text-h">Arrival of Hagrid : </span><span class="text-c">Brings Harry on flying motorcycle, leaves on Dursleys' doorstep</span></li>
      </ul>
    </li>
  <li><span class="text-h">Protection of the Sorcerer's Stone : </span><span class="text-c">Challenges set by professors to prevent theft</span></li>
    </ul>
  </li>
  <li><span class="caret">Locations : </span>
    <ul class ="nested">
  <li><span class="text-h">Privet Drive : </span><span class="text-c">Dursleys' residence and where Harry is left</span></li>
  <li><span class="text-h">Hogwarts : </span><span class="text-c">Integral setting for the narrative, where challenges and character development occur</span></li>
    </ul>
  </li>
  <li><span class="caret">Objects and Artifacts : </span>
    <ul class ="nested">
  <li><span class="text-h">The Sorcerer's Stone : </span><span class="text-c">Grants immortality, wealth, central to Voldemort's plot and protections</span></li>
    </ul>
  </li>
  <li><span class="caret">TemporalSetting : </span>
    <ul class ="nested">
  <li><span class="text-h">General Timeline : </span><span class="text-c">Nearly ten years since the start, events take place over Harry's first year at Hogwarts</span></li>
  <li><span class="text-h">Upcoming Timeframe : </span><span class="text-c">Looking forward to future events set in the summer</span></li>
    </ul>
  </li>
  <li><span class="caret">Tone : </span>
    <ul class ="nested">
  <li><span class="text-h">Playfulness : </span><span class="text-c">Light-hearted interactions implied throughout</span></li>
  <li><span class="text-h">Anticipation and Closure : </span><span class="text-c">Closing of one chapter with hints of future adventures</span></li>
    </ul>
  </li>
  <li><span class="caret">Narrative : </span>
    <ul class ="nested">
  <li><span class="text-h">Closure : </span><span class="text-c">The end of the storyline with hints of continuity</span></li>
    <li><span class="caret">Character Details : </span>
      <ul class ="nested">
   <li><span class="text-h">Unspecified Narrator : </span><span class="text-c">Positive anticipation for future events involving Dudley</span></li>
      </ul>
    </li>
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

IS_DEMO = False