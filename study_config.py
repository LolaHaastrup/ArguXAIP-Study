"""
study_config.py
===============

Every piece of participant-facing text and the full questionnaire live here,
in one file, so that they can be checked against the approved ethics
application without reading any application code.

IMPORTANT
---------
The text below is a STRUCTURED PLACEHOLDER, not approved ethics copy. Every
string marked [REPLACE] must be replaced with the exact wording from the
Participant Information Sheet and Consent Form that the University of
Huddersfield ethics committee approved under ECR_2024_17. Text that looks
compliant but differs from the approved wording is a protocol deviation.

The one substantive value that is set rather than left blank is the data
retention period, which the study requires to be stated as ten years in
line with University policy. See RETENTION_YEARS below.
"""

# ---------------------------------------------------------------------------
# Study identification
# ---------------------------------------------------------------------------

STUDY_TITLE = (
    "Explaining Temporal Plans through Argumentation: "
    "An Evaluation of a Dialogue-Based Chatbot"
)

PROJECT_CODE = "ECR_2024_17"

RESEARCHER_NAME = "Omolola Oluyemisi Haastrup"
RESEARCHER_EMAIL = "Omololaoluyemisi.haastrup@hud.ac.uk"
SUPERVISOR_NAMES = "Dr Quratul-Ain Mahesar and Professor Mauro Vallati"
SCHOOL = "School of Computing and Engineering, University of Huddersfield"

# [REPLACE] with the reference issued by the ethics committee.
ETHICS_REFERENCE = "[REPLACE with your SREP / ethics approval reference]"

# [REPLACE] with the contact route named in your approved documents for
# complaints, which is normally not the researcher.
COMPLAINTS_CONTACT = "[REPLACE with the complaints contact named in your approved PIS]"

# ---------------------------------------------------------------------------
# Data retention
# ---------------------------------------------------------------------------
# The study is required to state a ten year retention period, in line with
# University of Huddersfield policy. This constant is the single source of
# truth: it is interpolated into the information sheet, the consent form and
# the debrief, so the three can never disagree with each other.

RETENTION_YEARS = 10

RETENTION_STATEMENT = (
    f"Research data collected in this study will be retained for "
    f"{RETENTION_YEARS} years, in line with University of Huddersfield "
    f"policy on the retention of research data. Data will be stored "
    f"securely and will be accessible only to the research team named "
    f"above. After {RETENTION_YEARS} years the data will be securely "
    f"destroyed."
)

# ---------------------------------------------------------------------------
# Participant information sheet
# ---------------------------------------------------------------------------
# Each entry is (heading, body). Bodies marked [REPLACE] are placeholders.

PARTICIPANT_INFORMATION = [
    (
        "What is this study about?",
        "[REPLACE] You are invited to take part in a research study about how "
        "artificial intelligence systems explain the plans and schedules they "
        "produce. You will use a chatbot that explains a travel plan, ask it "
        "questions about the plan, and then answer a short questionnaire about "
        "your experience.",
    ),
    (
        "Why have I been invited?",
        "[REPLACE] You have been invited because you are over 18 and are able "
        "to read and respond in English. No specialist knowledge of artificial "
        "intelligence or planning is required.",
    ),
    (
        "Do I have to take part?",
        "[REPLACE] No. Taking part is entirely voluntary. You may stop at any "
        "point by closing the browser window, without giving a reason and "
        "without any disadvantage to you.",
    ),
    (
        "What will I be asked to do?",
        "[REPLACE] You will read a short description of a travel plan, then "
        "use a chatbot to ask questions about why the plan is or is not valid. "
        "You will then complete a questionnaire. The session is expected to "
        "take approximately 20 to 30 minutes.",
    ),
    (
        "What data will be collected?",
        "[REPLACE] The study records the questions you ask the chatbot and the "
        "order in which you ask them, your questionnaire responses, and the "
        "time you spend on each part of the study. It does not record your "
        "name, your email address, your IP address, or any other information "
        "that identifies you directly.",
    ),
    (
        "Will my taking part be kept confidential?",
        "[REPLACE] Yes. You are identified only by a randomly generated "
        "participant code. That code cannot be traced back to you by the "
        "research team. Results will be reported in aggregate in a doctoral "
        "thesis and in academic publications, and no individual participant "
        "will be identifiable in any output.",
    ),
    (
        "How long will my data be kept?",
        RETENTION_STATEMENT,
    ),
    (
        "What if I want to withdraw?",
        "[REPLACE] You may stop at any time before you submit your responses "
        "simply by closing the window, and nothing will be recorded. Because "
        "responses are anonymous and carry no link to your identity, it will "
        "not be possible to identify and remove your data once you have "
        "submitted it. Check this wording against your approved application, "
        "since the withdrawal position must match exactly what was approved.",
    ),
    (
        "Who has reviewed this study?",
        f"[REPLACE] This study has been reviewed and approved by the ethics "
        f"committee of the {SCHOOL}, under project code {PROJECT_CODE}, "
        f"approval reference {ETHICS_REFERENCE}.",
    ),
    (
        "Who do I contact with questions or concerns?",
        f"[REPLACE] For questions about the research, contact "
        f"{RESEARCHER_NAME} at {RESEARCHER_EMAIL}. The project is supervised "
        f"by {SUPERVISOR_NAMES}. If you wish to raise a concern or make a "
        f"complaint about the conduct of this study, contact "
        f"{COMPLAINTS_CONTACT}.",
    ),
]

# ---------------------------------------------------------------------------
# Consent
# ---------------------------------------------------------------------------
# Every item must be ticked before the participant can proceed. The retention
# item is included explicitly because consent to the retention period must be
# recorded, not merely disclosed in the information sheet.

CONSENT_ITEMS = [
    "I confirm that I am 18 years of age or older.",
    "I confirm that I have read and understood the participant information "
    "above, and that I have had the opportunity to consider it.",
    "I understand that my participation is voluntary and that I am free to "
    "stop at any time before submitting my responses, without giving a reason.",
    "I understand that the questions I ask the chatbot, my questionnaire "
    "responses and my timings will be recorded, and that I will be identified "
    "only by a randomly generated participant code.",
    f"I understand that my anonymised research data will be retained for "
    f"{RETENTION_YEARS} years in line with University of Huddersfield policy, "
    f"and will then be securely destroyed.",
    "I understand that anonymised findings may be reported in a doctoral "
    "thesis and in academic publications, and that I will not be identifiable "
    "in any output.",
    "I agree to take part in this study.",
]

# ---------------------------------------------------------------------------
# Task instructions
# ---------------------------------------------------------------------------

TASK_INTRODUCTION = (
    "[REPLACE] On the next screen you will see a travel plan produced by an "
    "automated planner, and a chatbot that can explain it. The chatbot will "
    "first tell you whether the plan is valid. You can then put questions to "
    "it by choosing from the buttons shown. Only questions that make sense at "
    "that point in the conversation are offered, so the buttons will change as "
    "you go.\n\n"
    "Please ask as many or as few questions as you wish. There are no right or "
    "wrong choices. When you feel you understand the plan, or when you have no "
    "further questions, select **End dialogue** and continue to the "
    "questionnaire."
)

DEBRIEF = (
    "[REPLACE] Thank you for taking part.\n\n"
    "This study examined whether explanations built from formal argumentation, "
    "delivered as a dialogue rather than as a single block of text, help people "
    "understand and challenge the plans that automated planners produce. The "
    "chatbot you used was not generating explanations freely. Every answer it "
    "gave was drawn from a formal structure computed in advance, which is why "
    "it could tell you exactly which requirement a plan failed.\n\n"
    + RETENTION_STATEMENT
)

# ---------------------------------------------------------------------------
# Questionnaire
# ---------------------------------------------------------------------------
# Self-report items are grouped by construct. The constructs match those in
# the Year 2 report's user study groundwork.
#
# NOTE ON ITEM COUNT. The count reported in your written documents must equal
# len(all_items()) below, and the app displays that number so the two cannot
# drift. Two of the nine constructs in the Year 2 report, task performance and
# dialogue engagement, are BEHAVIOURAL measures derived from the dialogue
# transcript rather than self-report items. That distinction may account for
# the discrepancy between the item counts appearing in different documents,
# though I cannot confirm that from here. Reconcile it against the approved
# instrument before recruiting.

LIKERT_SCALE = [
    "Strongly disagree",
    "Disagree",
    "Neither agree nor disagree",
    "Agree",
    "Strongly agree",
]

QUESTIONNAIRE = [
    (
        "Comprehension",
        [
            "I understood why the plan was arranged in the order it was.",
            "I could follow the explanations the system gave me.",
            "The explanations used language I found clear.",
        ],
    ),
    (
        "Perceived correctness",
        [
            "I believe the system's verdict on the plan was correct.",
            "The evidence the system gave supported the verdict it reached.",
        ],
    ),
    (
        "Contestability",
        [
            "I felt able to challenge the system's claims about the plan.",
            "The system gave a direct answer when I questioned it.",
            "If I disagreed with the plan, I would know which part to question.",
        ],
    ),
    (
        "Transparency",
        [
            "It was clear to me what the system had checked.",
            "The system made clear which parts of the plan its verdict rested on.",
        ],
    ),
    (
        "Willingness to act",
        [
            "I would be willing to act on this plan.",
            "I would be comfortable letting this system plan on my behalf.",
        ],
    ),
    (
        "Trust",
        [
            "I trust the system's assessment of the plan.",
            "I would rely on this system to tell me when a plan will not work.",
            "The system seemed honest about the plan's weaknesses.",
        ],
    ),
    (
        "Satisfaction",
        [
            "I was satisfied with the explanations I received.",
            "The amount of detail was appropriate for my needs.",
            "I would use a system like this again.",
        ],
    ),
]

OPEN_QUESTIONS = [
    "What, if anything, did you find unclear about the system's explanations?",
    "Was there a question you wanted to ask the system but could not?",
    "Any other comments?",
]

# Behavioural measures taken from the dialogue transcript rather than asked.
BEHAVIOURAL_MEASURES = [
    "Task performance, derived from the critical questions raised against "
    "those available.",
    "Dialogue engagement, derived from dialogue depth, the ratio of "
    "drill-down moves to top-level challenges, and whether the participant "
    "closed early or exhausted the available questions.",
]


def all_items():
    """Flatten the questionnaire to (construct, item) pairs.

    The app reports len(all_items()) on screen, so the item count stated in
    the ethics application, the thesis and the app are derived from one list
    rather than asserted independently in three places.
    """
    return [
        (construct, item)
        for construct, items in QUESTIONNAIRE
        for item in items
    ]


# ---------------------------------------------------------------------------
# Domains
# ---------------------------------------------------------------------------
# Each entry names the artefact prefix in data/ and how the domain is described
# to a viewer. Adding a third domain is an entry here plus its four JSON files.

DOMAINS = {
    "bus_train": {
        "label": "Transport, bus and train journey",
        "short": "Transport",
        "blurb": "A passenger travels by bus to a station, waits on the "
                 "platform while the train arrives, then travels by train to "
                 "the destination. The planner has scheduled each step.",
    },
    "cash_transfer": {
        "label": "Social protection, cash transfer with grievance resolution",
        "short": "Social protection",
        "blurb": "A beneficiary is verified and approved for a cash transfer. "
                 "The first payment fails, a grievance is lodged and reviewed, "
                 "the record is corrected, and payment is re-authorised and "
                 "completed before the programme deadline.",
    },
}

#: The single domain the approved study protocol uses. Explore mode may show
#: any domain; the study must not vary from what was approved without an
#: ethics amendment.
STUDY_DOMAIN = "bus_train"
