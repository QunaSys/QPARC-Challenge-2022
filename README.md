![image2](https://user-images.githubusercontent.com/81676915/166094918-280c5d1b-a8e1-41e9-81cd-73ac42e4a545.jpg)

# QPARC-Challenge-2022
Submission repository for QPARC Challenge 2022 https://www.quantumcomputingchallenge.com/

# What is QPARC Challenge?
QPARC Challenge is an international hackathon for students, engineers, scientists, and any others who learn quantum information and chemistry around the world. Participants can access Qamuy, a quantum computing cloud service, to solve challenges in combination with other quantum chemistry calculation programs.
 
From 6th to 15th of May, participants will solve challenges related to material development. On 29th May, finalists are selected for the next step and prepare for a presentation for the final judge. On 3rd June, final judgement is held and finalists give a presentation of their solutions, which is judged by industrial and academic experts. Winners will be awarded 10,000 USD in total (5,000 USD for each Challenges) and Qamuy free license.

# What is new about QPARC Challenge?
## 1. Key concept  
  The unique point of the QPARC challenge is that we start from the existing “State-of-the-art algorithm”. While many other challenges introduce existing applications to which quantum algorithms can be applied, QPARC Challenge only sets industrial problems. You can use Qamuy  to perform numerous chemical simulations.

## 2. Challenges specific to your area of expertise  
  In OPARC Challenge, there are two types of challenges:

 - [Quantum Information Experts](https://github.com/QunaSys/QPARC-Challenge-2022/tree/main/Quantum-Information-Expert)
 - [Quantum Chemistry Experts](https://github.com/QunaSys/QPARC-Challenge-2022/tree/main/Quantum-Chemistry-Expert)
 
You can choose a challenge that is related to your area of ex.epertise or you're interested in. Aims and evaluation criteria for each type are shown in a table below.  

# Detail of QPARC Challenge

<table>
<tr>
  <th></th>
  <th>Quantum Information Expart</th>
  <th>Quantum Chemistry Expart</th>
<tr>
  <th>Challenge</th>
  <td>What’s the best way to speed-up for a given chemical system & algorithm?</td>
  <td>Which chemical system could be calculated most efficiently using a given algorithm?</td>
<tr>
  <td>Aim and expectation</td>
  <td align="left" valign="top">
   <ul>
    <li>VQE (Variational quantum eigensolver) is one of the most famous methods using NISQ devices to calculate quantum chemical problem. However, the problem is it takes huge time to get result due to the iterative character and the need for sampling during the parameter optimization process</li>
    <li>In this challenge, participants are expected to reduce the computational cost as much as possible for a given chemical system & algorithm.
     <ul><li>(e.g. use the methods like efficient circuit mapping or efficient parameter update)</li></ul>
    </li>
   </ul>
  </td>
  <td align="left" valign="top">
   <ul>
    <li>In VQE calculation, depending on the ansatz, we can get several unique characteristics which classical computer usually doesn’t have such as
     <ul>
      <li>The number of electron is not preserved and able to change throughout the reaction</li>
      <li>Spin multiplicity is not fixed and able to change throughout the reaction, and so on.</li>
     </ul>
    </li>
    <li>In this challenge, participants are expected to 
     <ol>
      <li>select a chemical system where the unique characteristics of quantum is mostly enhanced and</li>
      <li>demonstrate the idea.</li>
     </ol>  
     (You can use our chemical calculation software “Qamuy” to do the demonstration)
    </li>
   </ul>
  </td>
<tr>
  <td>Evaluation criteria</td>
  <td align="center" valign="middle">Total reduction of calculation time</td>
  <td align="center" valign="middle">Innovativeness of the system selection</td>
</table>
  
# Schedule
<table>
<tr>
  <th>Sun</th>
  <th>Mon</th>
  <th>Tue</th>
  <th>Wed</th>
  <th>Thu</th>
  <th>Fri</th>
  <th>Sat</th>
</tr>
<tr>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td>
    <b>May 6, 17:00-18:30 (JST)</b><br>
    Kick-off Event<br>
    <ul>
      <li>Overview and detailed description of Challanges - Tennin Yan
        <ul>
          <li>Detailed description of each Challenges (Quantum Information Expert / Quantum Chemistry Expert)</li>
          <li>Evalution criteria</li>
          <li>Awards, etc.</li>
        </ul>
      </li>
      <li>Quantum chemistry and quantum computer - Kosuke Mitarai</li>
      <li>Qamuy tutorial - Andreas Thomasen</li>
    </ul>
  </td>
  <td></td>
</tr>
<tr>
  <td><br></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
</tr>
<tr>
  <td>
    <b>May 15, 23:59 (JST)</b><br>
    1st deadline<br>
    *Participants who fished their project can submit by this date
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
</tr>
<tr>
  <td>
    <b>May 22, 23:59 (JST)</b><br>
    2nd deadline<br>
    finish Qamuy free trial period
  </td>
  <td colspan=6 align="center" valign="middle">
    <b>May 23 - May 29</b><br>
    Evaluation Phase
  </td>
</tr>
<tr>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td>
    <b>Jun 3, 17:00-20:00 (JST)</b><br>
    Final Judgement<br>
    <ul>
      <li></li>
      <li></li>
    </ul>
  </td>
  <td></td>
</tr>
</table>

# How to submit
To submit, simply open an Issue using this template summarizing your project. Specifically, this issue should contain:

Team name: Your team's name
Team members: Listup all members name
Applied challenge: Choose from: Chemistry Challenge Information Challenge In addition, please label this GitHub issue with the challenge you applied.
Project Description: A brief description of your project (1-2 paragraphs).
Presentation: A link of presentation of your team’s hackathon project (e.g., video, jupyter notebook, slideshow, etc.).
Source code: A link to the final source code for your team's hackathon project (e.g., a GitHub repo).

# Tutorials
