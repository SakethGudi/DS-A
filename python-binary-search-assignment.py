#!/usr/bin/env python
# coding: utf-8

# # Assignment 1 - Binary Search Practice
# 
# _This assignment is a part of the course ["Data Structures and Algorithms in Python"](https://jovian.ai/learn/data-structures-and-algorithms-in-python)._
# 
# In this assignment, you'll get to practice some of the concepts and skills covered in the following notebooks:
# 
# 1. [Binary Search and Complexity Analysis](https://jovian.ai/aakashns/python-binary-search)
# 3. [Solving Programming Problems Systematically](https://jovian.ai/aakashns/python-problem-solving-template)
# 
# As you go through this notebook, you will find a **???** in certain places. To complete this assignment, you must replace all the **???** with appropriate values, expressions or statements to ensure that the notebook runs properly end-to-end. 
# 
# Some things to keep in mind:
# 
# * Make sure to run all the code cells, otherwise you may get errors like `NameError` for undefined variables.
# * Do not change variable names, delete cells or disturb other existing code. It may cause problems during evaluation.
# * In some cases, you may need to add some code cells or new statements before or after the line of code containing the **???**. 
# * Since you'll be using a temporary online service for code execution, save your work by running `jovian.commit` at regular intervals.
# * Questions marked **(Optional)** will not be considered for evaluation, and can be skipped. They are for your learning.
# 
# You can make submissions on this page: https://jovian.ai/learn/data-structures-and-algorithms-in-python/assignment/assignment-1-binary-search-practice
# 
# 
# If you are stuck, you can ask for help on the community forum: https://jovian.ai/forum/c/data-structures-and-algorithms-in-python/assignment-1/87 . You can get help with errors or ask for hints, but **please don't ask for OR share the full working answer code** on the forum.
# 
# 

# ## How to run the code and save your work
# 
# The recommended way to run this notebook is to click the "Run" button at the top of this page, and select "Run on Binder". This will run the notebook on [mybinder.org](https://mybinder.org), a free online service for running Jupyter notebooks. 
# 
# This tutorial is an executable [Jupyter notebook](https://jupyter.org). You can _run_ this tutorial and experiment with the code examples in a couple of ways: *using free online resources* (recommended) or *on your computer*.
# 
# #### Option 1: Running using free online resources (1-click, recommended)
# 
# The easiest way to start executing the code is to click the **Run** button at the top of this page and select **Run on Binder**. You can also select "Run on Colab" or "Run on Kaggle", but you'll need to create an account on [Google Colab](https://colab.research.google.com) or [Kaggle](https://kaggle.com) to use these platforms.
# 
# 
# #### Option 2: Running on your computer locally
# 
# To run the code on your computer locally, you'll need to set up [Python](https://www.python.org), download the notebook and install the required libraries. We recommend using the [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) distribution of Python. Click the **Run** button at the top of this page, select the **Run Locally** option, and follow the instructions.
# 
# #### Saving your work
# 
# Before staring the assignment, let's save a snapshot of the assignment to your [Jovian](https://jovian.ai) profile, so that you can access it later, and continue your work.

# In[1]:


get_ipython().system('pip install jovian --upgrade --quiet')


# In[2]:


import jovian


# In[3]:


project='python-binary-search-assignment'


# In[4]:


jovian.commit(project=project, privacy='secret', environment=None)


# You may be asked to [provide an API Key](https://jovian.ai/docs/user-guide/upload.html) to upload your notebook. The privacy of your assignment notebook is set to "Secret", so that you can the evaluators can access it, but it will not shown on your public profile to other users. 
# 
# To continue working on a saved assignment, just visit [your profile](https://jovian.ai/) and run the saved notebook again.

# ## Problem - Rotated Lists
# 
# We'll solve the following problem step-by-step:
# 
# > You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list. You can assume that all the numbers in the list are unique.
# >
# > Example: The list `[5, 6, 9, 0, 2, 3, 4]` was obtained by rotating the sorted list `[0, 2, 3, 4, 5, 6, 9]` 3 times.
# >
# > We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list `[3, 2, 4, 1]` produces `[1, 3, 2, 4]`. 
# >
# >"Sorted list" refers to a list where the elements are arranged in the increasing order  e.g. `[1, 3, 5, 7]`.
# >

# ## The Method
# 
# Here's the systematic strategy we'll apply for solving problems:
# 
# 1. State the problem clearly. Identify the input & output formats.
# 2. Come up with some example inputs & outputs. Try to cover all edge cases.
# 3. Come up with a correct solution for the problem. State it in plain English.
# 4. Implement the solution and test it using example inputs. Fix bugs, if any.
# 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
# 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
# 
# This approach is explained in detail in [Lesson 1](https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-1-binary-search-linked-lists-and-complexity) of the course. Let's apply this approach step-by-step.

# ## Solution
# 
# 
# ### 1. State the problem clearly. Identify the input & output formats.
# 
# While this problem is stated clearly enough, it's always useful to try and express in your own words, in a way that makes it most clear for you. It's perfectly OK if your description overlaps with the original problem statement to a large extent.
# 
# <br/>
# 
# _**Q: Express the problem in your own words below (to edit this cell, double click on it).**_
# 
# **Problem**
# 
# > In the above problem we are given a random array of numbers, our task is to find a way to get the array by rotating the sorted list by a minimum no.of times(N).
# Eg. [4,5,3] is the given array we get this array by rotating [3,4,5] one time , thus N=1.
# 
# <br/>
# 
# _**Q: The function you write will take one input called `nums`. What does it represent? Give an example.**_
# 
# **Input**
# 
# 1. `nums`: It represents the random list of numbers which are given to us, in an unsorted way.
# Eg. [2,4,3,6,9,8,5]
# 
# <br/>
# 
# _**Q: The function you write will return a single output called `rotations`. What does it represent? Give an example.**_
# 
# **Output**
# 
# 3. `rotations`: It represents the minimum number of rotations of the original list to get the given list. It can be indicated by 'N'.
# Eg. [4,5,3] is the given array we get this array by rotating [3,4,5] one time , thus N=1.
# 
# <br/>
# 
# Based on the above, we can now create a signature of our function:

# In[5]:


def count_rotations(nums):
    pass


# After each, step remember to save your notebook

# In[6]:


jovian.commit(project=project)


# ### 2. Come up with some example inputs & outputs. Try to cover all edge cases.
# 
# Our function should be able to handle any set of valid inputs we pass into it. Here's a list of some possible variations we might encounter:
# 
# 1. A list of size 10 rotated 3 times.
# 2. A list of size 8 rotated 5 times.
# 3. A list that wasn't rotated at all.
# 4. A list that was rotated just once. 
# 5. A list that was rotated `n-1` times, where `n` is the size of the list.
# 6. A list that was rotated `n` times (do you get back the original list here?)
# 7. An empty list.
# 8. A list containing just one element.
# 9. (can you think of any more?)
# 
# We'll express our test cases as dictionaries, to test them easily. Each dictionary will contain 2 keys: `input` (a dictionary itself containing one key for each argument to the function and `output` (the expected result from the function). Here's an example.

# In[7]:


test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}


# We can test the function by passing the input to it directly or by using the `evaluate_test_case` function from `jovian`.

# In[31]:


nums0 = test['input']['nums']
output0 = test['output']
result0 = count_rotations(nums0)
result0, result0 == output0


# In[32]:


from jovian.pythondsa import evaluate_test_case


# In[33]:


evaluate_test_case(count_rotations, test)


# Let's create one test case for each of the scenarios listed above. We'll store our test cases in an array called `tests`.

# _**Q: Create proper test cases for each of the scenarios listed above.**_

# In[34]:


test0 = test


# In[52]:


# A list of size 8 rotated 5 times.
test1 = {
    'input': {
        'nums': [19,21,24,27,35,12,15,18]
    },
    'output': 5
}


# In[51]:


# A list that wasn't rotated at all.
test2 = {
    'input': {
        'nums': [2,4,7,8,9]
    },
    'output': 0
}


# A list that was rotated just once.
# A list that was rotated n-1 times, where n is the size of the list.
# A list that was rotated n times (do you get back the original list here?)
# An empty list.
# A list containing just one element.

# In[53]:


# A list that was rotated just once.
test3 = {
    'input': {
        'nums': [53,15,16,21,26,39,42,49]
    },
    'output': 1
}


# In[54]:


# A list that was rotated n-1 times, where n is the size of the list.
test4 = {
    'input': {
        'nums': [5,8,12,14,16,17,1]
    },
    'output': 6
}


# In[110]:


# A list that was rotated n times, where n is the size of the list
test5 = {
    'input': {
        'nums': [3,5,6,8,9,10]
    },
    'output': 0
}


# **HINT**: Read the question carefully to determine the correct output for the above test case.

# In[111]:


# An empty list.
test6 = {
    'input': {
        'nums': []
    },
    'output': 0
}


# In[112]:


# A list containing just one element.
test7 = {
    'input': {
        'nums': [2]
    },
    'output': 0
}


# In[113]:


tests = [test0, test1,test2, test3, test3, test5, test6, test7]


# _**Q (Optional): Include any further test cases below, for other interesting scenarios you can think of.**_

# In[ ]:





# In[ ]:





# Evaluate your function against all the test cases together using the `evaluate_test_cases` (plural) function from `jovian`.

# In[114]:


from jovian.pythondsa import evaluate_test_cases


# In[115]:


evaluate_test_cases(count_rotations, tests)


# Verify that all the test cases were evaluated. We expect them all to fail, since we haven't implemented the function yet.
# 
# Let's save our work before continuing.

# In[116]:


jovian.commit(project=project)


# ### 3. Come up with a correct solution for the problem. State it in plain English.
# 
# Our first goal should always be to come up with a _correct_ solution to the problem, which may not necessarily be the most _efficient_ solution. Try to think of a solution before you read further. 
# 
# Coming up with the correct solution is quite easy, and it's based on this insight: If a list of sorted numbers is rotated `k` times, then the smallest number in the list ends up at position `k` (counting from 0). Further, it is the only number in the list which is smaller than the number before it. Thus, we simply need to **check for each number in the list whether it is smaller than the number that comes before it** (if there is a number before it). Then, our answer i.e. the number of rotations is simply the position of this number is . If we cannot find such a number, then the list wasn't rotated at all.
# 
# Example: In the list `[19, 25, 29, 3, 5, 6, 7, 9, 11, 14]`, the number `3` is the only number smaller than its predecessor. It occurs at the position `4` (counting from `0`), hence the array was rotated `4` times.
# 
# 
# We can use the *linear search* algorithm as a first attempt to solve this problem i.e. we can perform the check for every position one by one. But first, try describing the above solution in your own words, that make it clear to you.
# 
# _**Q (Optional): Describe the linear search solution explained above problem in your own words.**_
# 
# 1. **???**
# 2. **???**
# 3. **???**
# 4. **???**
# 
# (add more steps if required)
# 
# 
# Let's save and upload our work before continuing.

# In[117]:


import jovian


# In[118]:


jovian.commit(project=project)


# ###  4. Implement the solution and test it using example inputs. Fix bugs, if any.
# 
# _**Q: Implement the solution described in step 3.**_

# In[119]:


def count_rotations_linear(nums):
    position = 1                # What is the intial value of position?
    
    while position<len(nums):                     # When should the loop be terminated?
        
        # Success criteria: check whether the number at the current position is smaller than the one before it
        if position > 0 and nums[position] < nums[position-1]:   # How to perform the check?
            return position
        else:
        # Move to the next position
           position += 1
    
    return 0                     # What if none of the positions passed the check               


# Let's test out the function with the first test case.

# In[120]:


linear_search_result = evaluate_test_case(count_rotations_linear, test)


# Make sure your function passes the test. Fix bugs, if any. 
# 
# Let's test it out with all the test cases.

# In[121]:


linear_search_results = evaluate_test_cases(count_rotations_linear, tests)


# Once again, make sure all the tests pass. Fix errors and bugs, if any.
# 
# **NOTE**: During evaluation, your submission will be tested against a much larger set of test cases (not listed here). Make sure to test your solution thoroughly.
# 
# If you are stuck, you can ask for help on the community forum: https://jovian.ai/forum/c/data-structures-and-algorithms-in-python/assignment-1/87 . You can get help with errors or ask for hints, but **please don't ask for OR share the full working answer code** on the forum.

# ### 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
# 
# Count the maximum number of iterations it may take for the algorithm to return the result.
# 
# _**Q: What is the worst-case complexity (running time) of the algorithm expressed in the Big O Notation? Assume that the size of the list is `N` (uppercase).**_
# 

# In[125]:


linear_search_complexity = "O(N)"


# ### 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
# 
# As you might have guessed, we can apply _Binary Search_ to solve this problem. The key question we need to answer in binary search is: Given the middle element, how to decide if it is the answer (smallest number), or whether the answer lies to the left or right of it. 
# 
# If the middle element is smaller than its predecessor, then it is the answer. However, if it isn't, this check is not sufficient to determine whether the answer lies to the left or the right of it. Consider the following examples.
# 
# `[7, 8, 1, 3, 4, 5, 6]` (answer lies to the left of the middle element)
# 
# `[1, 2, 3, 4, 5, -1, 0]` (answer lies to the right of the middle element)
# 
# Here's a check that will help us determine if the answer lies to the left or the right: _If the middle element of the list is smaller than the last element of the range, then the answer lies to the left of it. Otherwise, the answer lies to the right._
# 
# Do you see why this strategy works?
# 

# ### 7. Come up with a correct solution for the problem. State it in plain English.
# 
# Before we implement the solution, it's useful to describe it in a way that makes most sense to you. In a coding interview, you will almost certainly be asked to describe your approach before you start writing code.
# 
# _**Q (Optional): Describe the binary search solution explained above problem in your own words.**_
# 
# 1. **???**
# 2. **???**
# 3. **???**
# 4. **???**
# 
# (add more steps if required)
# 
# Let's save and upload our work before continuing.

# In[126]:


jovian.commit(project=project)


# ### 8. Implement the solution and test it using example inputs. Fix bugs, if any.
# 
# *__Q: Implement the binary search solution described in step 7.__*
# 
# If you are stuck, you can ask for help on the community forum: https://jovian.ai/forum/c/data-structures-and-algorithms-in-python/assignment-1/87 . You can get help with errors or ask for hints, but **please don't ask for OR share the full working answer code** on the forum.

# In[133]:


def count_rotations_binary(nums):
    lo = 0
    hi = len(nums)-1
    
    while lo<=hi:
        mid = (lo+hi)//2
        mid_number = nums[mid]
        
        # Uncomment the next line for logging the values and fixing errors.
        # print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid > 0 and nums[mid]<nums[mid-1]:
            # The middle position is the answer
            return mid
        
        elif nums[mid]<nums[len(nums)-1]:
            # Answer lies in the left half
            hi = mid - 1  
        
        else:
            # Answer lies in the right half
            lo = mid + 1
    
    return 0


# Let's test out the function with the first test case.

# In[134]:


binary_search_result = evaluate_test_case(count_rotations_binary, test)


# Make sure your function passes the test. Fix bugs, if any.
# 
# Let's test it out with all the test cases.

# In[135]:


binary_search_results = evaluate_test_cases(count_rotations_binary, tests)


# Once again, make sure all the tests pass. Fix errors and bugs, if any.
# 
# **NOTE**: During evaluation, your submission will be tested against a much larger set of test cases (not listed here). Make sure to test your solution thoroughly.
# 
# If you are stuck, you can ask for help on the community forum: https://jovian.ai/forum/c/data-structures-and-algorithms-in-python/assignment-1/87 . You can get help with errors or ask for hints, but **please don't ask for OR share the full working answer code** on the forum.
# 
# Let's save our work before continuing.

# In[136]:


jovian.commit(project=project)


# ### 9. Analyze the algorithm's complexity and identify inefficiencies, if any.
# 
# _**Q: What is the worst-case complexity (running time) of the algorithm expressed in the Big O Notation? Assume that the size of the list is `N` (uppercase).**_
# 
# Hint: Count the maximum number of iterations it may take for the algorithm to return the result.

# In[137]:


binary_search_complexity = "O(log N)"


# Is binary search the optimal solution to the problem? How can you prove it? Discuss in the forums.
# 
# Let's save our work before continuing.

# In[138]:


import jovian


# In[139]:


jovian.commit()


# ## Make a Submission
# 
# To make a submission, visit the [assignment page](https://jovian.ai/learn/data-structures-and-algorithms-in-python/assignment/assignment-1-binary-search-practice) and submit the link to your notebook.
# 
# You can also make a submission by executing the following statement:

# In[ ]:


jovian.submit(assignment="pythondsa-assignment1")


# You can view your previous submissions under the "Submission History" section of the [assignment page](https://jovian.ai/learn/data-structures-and-algorithms-in-python/assignment/assignment-1-binary-search-practice). Only your last sumission will be considered for evaluation.

# ## Bonus Questions
# 
# The questions in this section are optional, and will not affect your grade. Discuss the bonus questions here: https://jovian.ai/forum/t/optional-bonus-questions-discussion-assignment-1/15486
# 
# You can also copy over the bonus questions to a new notebook to share your solution on the forum without sharing your assignment notebook. Duplicate this template: https://jovian.ai/aakashns/python-problem-solving-template
# 
# 
# ### Optional Bonus 1: Using the Generic Binary Search Algorithm
# 
# The `jovian` library provides a generic implementation of the binary search algorithm.

# In[ ]:


from jovian.pythondsa import binary_search


# You can view it's source code using the `??` command in Jupyter or on [the Github repository](https://github.com/JovianML/jovian-py/blob/master/jovian/pythondsa/__init__.py#L68) for the `jovian` library.

# In[ ]:


get_ipython().run_line_magic('pinfo2', 'binary_search')


# _**Q (Optional): Implement the `count_rotations` function using the generic `binary_search` function.**_
# 
# Hint: You'll need to define the condition which returns `"found"`, `"left"` or `"right"` by performing the appropriate check on the middle position in the range.

# In[ ]:


def count_rotations_generic(nums):
    def condition(mid):
        pass # replace this with your code
        
    return binary_search(0, len(nums)-1, condition)


# In[ ]:


evaluate_test_case(count_rotations_generic, test)


# In[ ]:


evaluate_test_cases(count_rotations_generic, test)


# In[ ]:


jovian.commit()


# Discuss your solution on the forum: https://jovian.ai/forum/c/data-structures-and-algorithms-in-python/assignment-1/87

# ### Optional Bonus 2: Handling repeating numbers
# 
# So far we've assumed that the numbers in the list are unique. What if the numbers can repeat? E.g. `[5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]`. Can you modify your solution to handle this special case?
# 
# 
# _**Q (Optional): Create additional test cases where the list can contain repeating numbers**_

# In[ ]:


extended_tests = list(tests)


# In[ ]:


extended_test.append({
    # add your test case here
})


# In[ ]:


extended_test.append({
    # add your test case here
})


# In[ ]:


# add more test cases if required


# In[ ]:


jovian.commit()


# _**Q (Optional): Modify your solution (if required) to handle the case where the list can contain repeating numbers.**_

# In[ ]:


def count_rotations_generic(nums):
    pass # replace this with your code


# Test your function to make sure it works properly.

# In[ ]:





# In[ ]:





# Discuss your solution on the forum: https://jovian.ai/forum/c/data-structures-and-algorithms-in-python/assignment-1/87

# ### Optional Bonus 3: Searching in a Rotated List
# 
# Here's a slightly advanced extension to this problem:
# 
# > You are given list of numbers, obtained by rotating a sorted list an unknown number of times. You are also given a target number. Write a function to find the position of the target number within the rotated list. You can assume that all the numbers in the list are unique.
# >
# > Example: In the rotated sorted list `[5, 6, 9, 0, 2, 3, 4]`, the target number `2` occurs at position `5`.

# **Q (Optional): Create some test cases for the above problem.**

# In[ ]:


tests2 = []


# In[ ]:


# add test cases here


# In[ ]:





# **Q (Optional): Implement a solution to the above problem using binary search.**
# 
# _HINT:_ One way to solve this problem is to identify two sorted subarrays within the given array (using the `count_rotations_binary` function defined above), then perform a binary search on each subarray to determine the position of the target element. Another way is to modify `count_rotations_binary` to solve the problem directly.

# In[ ]:


def find_element(nums, target):
    pass 


# Test your solution using the cells below.

# In[ ]:





# You can test your solution to the above problem here: https://leetcode.com/problems/search-in-rotated-sorted-array/
# 
# Discuss your approach on the forum: https://jovian.ai/forum/c/data-structures-and-algorithms-in-python/assignment-1/87

# In[ ]:


jovian.commit()

