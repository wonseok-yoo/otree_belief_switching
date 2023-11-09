# otree_belief_switching

This is a full code for my job market paper on "Belief Updating Under Cognitive Dissonance: An Experimental Study"

- Abstract -
  
Cognitive dissonance refers to the psychological tension that arises when individuals hold two conflicting beliefs, views, or actions simultaneously, and within a financial decision-making context, this tension may arise when a subject’s beliefs and asset choices conflict. We investigate the dynamics of belief updating in a setting where cognitive dissonance could play a significant role, by designing an experiment with four treatments. The first treatment simply elicits beliefs. In the subsequent three treatments, subjects are endowed with one of two potential assets at random. Following this, they are asked to report their beliefs regarding their assigned asset after each signal. Subjects have the option to either “switch” or “keep” their initial asset, with associated costs that vary across the three latter treatments (zero, finite, or infinite). By manipulating switching costs, we effectively intensify subjective ownership towards the asset, fostering cognitive dissonance. Our findings indicate that subjects frequently make sub-optimal asset choice decisions when confronted with a finite transaction cost. Furthermore, they tend to distort their beliefs about their endowed asset, aligning their beliefs with their sub-optimal actions to mitigate cognitive dissonance.

< Setting of the Experiment >

There are two assets: One asset is of High Value ($3), and the other asset is of Low Value ($1).

The two assets contain different number of balls. High Value Asset contains 6 Green balls, and 3 Red balls, whereas Low Value Asset contains 6 Red balls, and 3 Green balls.

The experimenter will randomly select one of the two assets following the prior which is communicated clearly to the subjects. 

Then, one ball will be selected from the chosen asset and shown to the subjects.

Subjects will report their subjective beliefs on the probability that the chosen asset is the High Value Asset.

The chosen ball is returned to the box and another ball will be drawn from the same box. 

This information provision process is repeated for 5 rounds. 

- Task 0 -

In Task 0, the value of the chosen asset is not relevant to the subjects because subjects payments do not depend on the value of the assets. 

Subjects payments only depend on the accuracy of their reporte beliefs. They report their beliefs before they see any signal (the only information is the prior), and for 5 rounds after each draw of the ball resulting in 6 reports for each prior. We have 3 priors, so in total, they report their report 18 times in this task 0. 

After the task is over, one of the rounds will be randomly selected and subjects will be paid for the reported beliefs for that particular round only. 

We use Binarized Scoring Rule as in Hossain et al (2013). 

- Task 1 and Task 2 -

In Task 1, and 2, in addition to 5 rounds of information provision and belief elicitaiton in Task 0, subjects are allowed to choose to "swap" or "keep" their chosen asset. 

In these tasks, subjects payments may depend on the value of their assets. This implies that subjects will care about the value of their assets which may induce behavioral biases. 

The only difference between Task 1 and Task 2 is that in Task 1, subjects enjoy the luxury of free transactions, whereas in Task 2, subjects are required to pay transaction costs ($1). 

I create more frictions in transaction through transaction costs, but in addition to that, I am injecting more subjective ownership to subjects. 

When subjects have to pay for an alternative, they feel they have more stake in the asset they currently hold. Therefore, subjects will have more hesitations (more behavioral bias, in addition to pure effects from changed economic incentives) to switch if they have switching costs compared to free switching scenario. 

We find that subjects indeed hesitate to switch, and moreover, they cater their beliefs in order to support their actions in Task 2, which I call, costly switching treatment in the paper. 

In particular, subjects who were supposed to switch when they were Bayesian, inflated their subjective beliefs so that their beliefs are aligned with their sub-optimal action ("Keep")

- Taks 3 -

In Task 3, subjects payments may depend on the value of the assets, but they are not allowed to switch. In this sense, subjects have the highest degree of subjective ownership. 

However, the lack of options in changing actions regulates the potential distortion of their beliefs, which result in no particular belief distortion as in Task 2. 



