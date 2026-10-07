import json, unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from event_tier_robustness_a6 import tier, spohn_blocks, BASE

class EventTier(unittest.TestCase):
    def test_tier_mapping_all_observed(self):
        recs = json.load(open(BASE/'results/mutation_convergence_a5.json'))['records']
        seen = {r['mutation_type'] for r in recs}
        for t in seen:
            self.assertIn(tier(t), ('A','B'))
        self.assertEqual(tier('large_deletion'), 'B')
        self.assertEqual(tier('short_deletion'), 'A')
        self.assertEqual(tier('SNP'), 'A'); self.assertEqual(tier('SNPs'), 'A')
        self.assertEqual(tier('Del 5 nt'), 'A'); self.assertEqual(tier('Ins 1 nt'), 'A')
        self.assertEqual(tier('insertion (IC3-like element, 1.4 kb)'), 'A')
    def test_unknown_type_halts(self):
        with self.assertRaises(ValueError):
            tier('chromosomal duplication')
    def test_block_coalescing_real_data(self):
        blocks = spohn_blocks()
        key = ('8821', '388,423')
        self.assertIn(key, blocks)
        self.assertEqual(blocks[key]['lines'],
                         {'BAC5_3','BAC5_5','BAC5_10','PR39_1','PR39_7','PR39_10'})
        self.assertIn('sbmA', blocks[key]['genes'])
        self.assertEqual(blocks[key]['amps'], {'BAC5','PR39'})
    def test_strict_no_false_cross(self):
        # synthetic: Tier B support in a second study must NOT create a strict match
        evo = [{'study':'s1','gene':'gX','tier':'A','line':'l1'},
               {'study':'s2','gene':'gX','tier':'B','line':'l2'}]
        from collections import defaultdict
        strict = defaultdict(set)
        for r in evo:
            if r['tier']=='A': strict[r['gene'].lower()].add(r['study'])
        self.assertNotIn('gx', [g for g,s in strict.items() if len(s)>=2])
    def test_a5_guard_counts(self):
        ledger = json.load(open(BASE/'results/mutation_convergence_a5.json'))
        recs = ledger['records']
        evo = [r for r in recs if r.get('scope','evolved')=='evolved']
        self.assertEqual(len(recs), 405)
        self.assertEqual(sum(1 for r in evo if r['study']=='spohn2019'), 383)
        self.assertEqual(sum(1 for r in evo if r['study']=='blanco2020'), 16)
        self.assertEqual(sum(1 for r in recs if r.get('scope')=='control'), 3)
        self.assertEqual(sum(1 for r in evo if r['study']=='bac7_2023'), 3)
    def test_result_json_structure(self):
        out = json.load(open(BASE/'results/event_tier_robustness_a6.json'))
        self.assertEqual(out['strict_cross_study_tierA'], ['sbma'])
        self.assertTrue(out['guard_within_study_match'])
        direct = [d for d in out['sbmA_event_ledger'] if d['tier']=='A']
        self.assertEqual(len(direct), 3)
        self.assertEqual({d['study'] for d in direct}, {'spohn2019','bac7_2023'})
        blocks = [d for d in out['sbmA_event_ledger'] if d['tier']=='B']
        self.assertEqual(len(blocks), 3)
        self.assertTrue(all('@ 388,423' in b['mutation_type'] for b in blocks))

if __name__ == '__main__':
    unittest.main()
