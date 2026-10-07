import importlib.util, unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('a5',Path(__file__).resolve().parents[1]/'scripts/mutation_convergence_a5.py')
a5=importlib.util.module_from_spec(spec);spec.loader.exec_module(a5)
class Convergence(unittest.TestCase):
 def test_clean_gene(self):
  self.assertEqual(a5.clean_gene('aceE →'),'aceE')
  self.assertEqual(a5.clean_gene('basS\xa0←'),'basS')
 def test_recurrence_and_control_exclusion(self):
  recs=[{'study':'s','amp':'a','gene':'g1','line':'l1','scope':'evolved','mutation_type':'SNPs'},
        {'study':'s','amp':'a','gene':'g1','line':'l2','scope':'evolved','mutation_type':'SNPs'},
        {'study':'s','amp':'a','gene':'g1','line':'l3','scope':'control','mutation_type':'SNPs'},
        {'study':'t','amp':'a','gene':'g1','line':'x1','scope':'evolved','mutation_type':'SNPs'}]
  within,cross=a5.recurrence(recs)
  self.assertEqual(len(within),1)
  self.assertEqual(within[0]['n_lines'],2)  # control line must not count
  self.assertEqual(cross,[{'gene':'g1','studies':['s','t']}])
 def test_no_false_cross(self):
  recs=[{'study':'s','amp':'a','gene':'g1','line':'l1','scope':'evolved','mutation_type':'SNPs'},
        {'study':'s','amp':'b','gene':'g1','line':'l2','scope':'evolved','mutation_type':'SNPs'}]
  self.assertEqual(a5.recurrence(recs)[1],[])
 def test_large_deletion_flag(self):
  recs=[{'study':'s','amp':'a','gene':'g','line':f'l{i}','scope':'evolved','mutation_type':'large_deletion'} for i in range(3)]
  self.assertTrue(a5.recurrence(recs)[0][0]['driven_by_large_deletion'])
 def test_case_insensitive_cross(self):
  recs=[{'study':'s','amp':'a','gene':'SbmA','line':'l1','scope':'evolved','mutation_type':'SNPs'},
        {'study':'t','amp':'b','gene':'sbmA','line':'l2','scope':'evolved','mutation_type':'SNPs'}]
  self.assertEqual(a5.recurrence(recs)[1],[{'gene':'sbma','studies':['s','t']}])
if __name__=='__main__':unittest.main()
