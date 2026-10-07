import importlib.util, math, unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('a4',Path(__file__).resolve().parents[1]/'scripts/blanco_intervals_a4.py')
a4=importlib.util.module_from_spec(spec);spec.loader.exec_module(a4)
class Intervals(unittest.TestCase):
 def test_exact(self):
  self.assertEqual(a4.transform(a4.parse('8'),2)['lower'],2)
 def test_censored(self):
  x=a4.transform(a4.parse('>60'),7.5)
  self.assertEqual(x,{'lower':3,'upper':None,'lower_open':True,'upper_open':True})
 def test_median(self):
  x=a4.median_interval([a4.parse('2')]*3+[a4.parse('>2')]*5)
  self.assertEqual(x,{'lower':2,'upper':None,'lower_open':True,'upper_open':True})
 def test_mixed_middle(self):
  self.assertTrue(a4.median_interval([a4.parse('2'),a4.parse('>2')])['lower_open'])
 def test_all_exact(self):
  self.assertEqual(a4.median_interval([a4.parse('2'),a4.parse('4')])['lower'],3)
 def test_malformed(self):
  for s in ['0','-1','nan','inf','>=2','2-4','<2','']:
   with self.assertRaises(ValueError):a4.parse(s)
 def test_empty(self):
  with self.assertRaises(ValueError):a4.median_interval([])
 def test_reference(self):
  with self.assertRaises(ValueError):a4.transform(a4.parse('2'),0)
if __name__=='__main__':unittest.main()
