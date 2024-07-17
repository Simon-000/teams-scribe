# Define prompt for turning vtt transcripts into case studies
def grab_vtt_into_case_study_prompt():
    turn_vtt_into_case_study_prompt = """
---

**Prompt for Case Study Generation from Teams Recording Transcript**

---

**Objective:**  
Transform the provided VTT transcript of a Teams recording into a detailed project case study.

---

**Audience:**  
The primary audience for this case study includes all employees of the consultancy, with a particular focus on the sales and marketing teams.

---

**Purpose:**  
The case study will be utilized to generate sales, marketing, and recruitment materials.

---

**Guidelines:**

1. **Introduction:**
   - Provide a brief overview of the project.
   - Include the project's objectives and scope.

2. **Project Background:**
   - Describe the client and their industry.
   - Explain the challenges or problems faced by the client.

3. **Project Execution:**
   - Detail the steps taken to address the client's challenges.
   - Highlight the strategies and methodologies used.
   - Include key milestones and timelines.

4. **Delivery Format:**
   - Describe the timeline and stages of the project.
   - Example: 3 weeks - Proof of Concept, 2 months - Discovery, 6 months - Alpha.

5. **Team Composition:**
   - Provide details on the team members involved in the project.
   - Example: 1x Data Scientist, 2x Business Analyst, 1x Project Manager.

6. **Technical Solution:**
   - Detail the technical solutions developed during the project.
   - Use sub-sections for each technical solution if there were multiple.

   **Example Sub-sections:**
   - **Cloud Environment:** Describe the cloud infrastructure set up for the project.
   - **Machine Learning Model:** Detail the development and deployment of any ML models.
   - **Data Warehouse Migration:** Explain the process and benefits of migrating to a new data warehouse.

7. **Results and Outcomes:**
   - Present the results achieved.
   - Use specific data and metrics to quantify success.
   - Share client feedback or testimonials if available.

8. **Lessons Learnt:**
   - Highlight key insights and learnings from the project.
   - Example: Discovery turned to proof of concept which meant insufficient time was spent on investigating the wider ecosystem, impacting delivery.

9. **Conclusion:**
   - Summarize the key takeaways from the project.
   - Emphasize the value delivered to the client.

10. **Visuals and Quotes:**
    - Incorporate relevant visuals (e.g., charts, graphs, images) to enhance the narrative.
    - Include direct quotes from the transcript where appropriate.

11. **Formatting:**
    - Ensure the case study is structured in clear, logical sections.
    - Use headings and subheadings to organize content.
    - Aim for a professional and engaging writing style.

---

**Instructions:**

1. Carefully review the provided VTT transcript of the Teams recording.
2. Extract key information and quotes from the transcript to support each section of the case study.
3. Write the case study in a detailed and engaging manner, ensuring it covers all the guidelines outlined above.
4. Aim for clarity, coherence, and a professional tone throughout the document.
5. Ensure the final case study is free of grammatical errors and typos.

---

**Example:**

---

**Project Case Study: [Project Name]**

**Introduction:**  
The [Project Name] project aimed to [brief description of project objectives]. The consultancy collaborated with [Client Name], a leading company in [Client's Industry], to tackle [specific challenges].

**Project Background:**  
[Client Name], a prominent player in [Client's Industry], was facing [specific challenges]. These challenges included [detailed description of the problems].

**Project Execution:**  
To address these challenges, our team implemented [strategies and methodologies]. Key steps included [detailed steps and processes]. Major milestones were achieved at [specific timelines].

**Delivery Format:**  
The project was structured in several phases:
- 3 weeks: Proof of Concept
- 2 months: Discovery
- 6 months: Alpha

**Team Composition:**  
The project team consisted of:
- 1x Data Scientist
- 2x Business Analyst
- 1x Project Manager

**Technical Solution:**  
Several technical solutions were developed during the project:

- **Cloud Environment:**  
  The cloud infrastructure was set up using [specific cloud platform]. This included [details of the infrastructure setup, such as servers, storage, networking].

- **Machine Learning Model:**  
  We developed and deployed a machine learning model to [brief description of the model's purpose and functionality]. The model was trained using [details of the data and training process].

- **Data Warehouse Migration:**  
  The migration to a new data warehouse involved [details of the migration process]. This resulted in [benefits of the new data warehouse, such as improved performance, scalability].

**Results and Outcomes:**  
The project successfully delivered [specific results], including [data and metrics]. Client feedback highlighted [specific testimonials or feedback].

**Lessons Learnt:**  
Several key insights were gained during the project:
- Discovery turned to proof of concept which meant insufficient time was spent on investigating the wider ecosystem, impacting delivery.

**Conclusion:**  
The [Project Name] project demonstrated [key takeaways]. The consultancy provided significant value by [summary of benefits delivered to the client].

**Visuals and Quotes:**  
![Chart illustrating project success](image_url)  
_"[Direct quote from transcript]"_

---
"""

    return turn_vtt_into_case_study_prompt