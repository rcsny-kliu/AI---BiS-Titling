# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:10:51 2019

@author: Kevin Liu
"""

import unittest
from bisProcess import *

class bisTests(unittest.TestCase):
    """Initialization Unit Tests"""
    def test_modInstall(self):
        #All modules are loaded correctly
        self.assertTrue(modInstall())
    
    """Text Processing Unit Tests"""
    def test_remove_stop(self):
        #Stopwords are removed
        self.assertEqual(remove_stop(['the','fox','would','run','faster','if','smaller']), ['fox', 'would', 'run', 'faster', 'smaller'])

    def test_remove_punc(self):
        #punctuations are removed
        self.assertEqual(remove_punc("The email address shouldn't be 123_321@email.com!"),'The email address shouldnt be 123321emailcom')
        
    def test_split_punc(self):
        #A sentence will be split into a list format by punctuation including space
        self.assertEqual(split_punc("apples, oranges, and other fruits"),["apples","oranges","and","other","fruits"])

    def test_pos_only(self):
        #Parts of Speech are properly excluded
        self.assertEqual(pos_only(["1","I","One","Uno"],'ex',['CD'],1),['I', 'Uno'])
        self.assertEqual(pos_only(["1","I","One","Uno"],'ex',['CD'],2),[('I', 'PRP'), ('Uno', 'NN')])
        #Parts of Speech are properly included
        self.assertEqual(pos_only(["1","I","One","Uno"],'in',['CD'],1),['1', 'One'])
        self.assertEqual(pos_only(["1","I","One","Uno"],'in',['CD'],2),[('1', 'CD'), ('One', 'CD')])

    def test_split_url(self):
        self.assertEqual(split_url("https://www.test-website.com/info1/info2_info3"),['www.test-website.com', 'info1'])

    def test_fuzz_comp(self):
        self.assertEqual(fuzz_comp('word1','word2','ratio'),[80])
        self.assertEqual(fuzz_comp('word1','word1 in word2','partial'),[100])
        self.assertEqual(fuzz_comp('word1','word1 in word2','weighted'),[76.5])
        
    def test_scoreCount(self):
        self.assertEqual(scoreCount([0,1,2,3,4],2),3)
        self.assertEqual(scoreCount([0,1,2,3,4],5),0)
        
    def test_scorePerc(self):
        self.assertEqual(scorePerc([0,1,2,3,4],2),3/5)
        self.assertEqual(scorePerc([0,1,2,3,4],5),0)
        
    def test_repAbb(self):
        self.assertEqual(repAbb("RCSworks.com"),"rcsworks")
        self.assertEqual(repAbb("rcsworks.com"),"rcsworks")
        self.assertEqual(repAbb("RCSworks & MediaMonitors"),"rcsworks and mediamonitors")

    def test_stateAbb(self):
        self.assertEqual(stateAbb("Not a State"),"not a state")
        self.assertEqual(stateAbb("Alabama"),"AL")
        self.assertEqual(stateAbb("The State Alabama"),"the state AL")
    
    def test_remove_spec(self):
        self.assertEqual(remove_spec("Remove the special character: \U000001a9"),"Remove the special character: ")
    
unittest.main()
