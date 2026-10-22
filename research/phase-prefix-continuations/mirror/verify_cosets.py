#!/usr/bin/env python3
"""Exact base-word/coset checks supporting the uniform graph obstruction."""
import argparse,hashlib,json,sys,types
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
ARITHMETIC_SHA='0d277854396e4ceda1e0f26916bd576b6decb474c0692b6671ebf2595283ddb9'
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--arithmetic',type=Path,default=ROOT.parent/'arithmetic.py')
p.add_argument('--words',type=Path,default=ROOT/'WORDS.json')
p.add_argument('--out',type=Path)
a=p.parse_args();payload=a.arithmetic.read_bytes()
if hashlib.sha256(payload).hexdigest()!=ARITHMETIC_SHA:raise ValueError('arithmetic dependency SHA256 mismatch')
v=types.ModuleType('arithmetic');exec(compile(payload,str(a.arithmetic),'exec'),v.__dict__)
data=json.loads(a.words.read_text())
base={name:v.monomial(d['permutation'],d['phase_i']) for name,d in data['free_base_letters'].items()}
base.update({f'C{i}':v.c_letter(i) for i in range(3)})
def expand(word):
 result=[]
 for name in word:result.extend(expand(data['derived_words'][name]) if name in data['derived_words'] else [name])
 return result
def W(*word):return v.word(*(base[name] for name in expand(word)))
def describe(matrix):
 support=[sum(z!=v.ZERO for z in row) for row in matrix]
 free=all(n==1 for n in support) and all(sum(matrix[i][j]!=v.ZERO for i in range(8))==1 for j in range(8)) and all(z==v.ZERO or z in v.I_POWERS for row in matrix for z in row)
 return {'row_support':support,'fourth_root_monomial':free}
K=W('K');C1=W('C1');C2=W('C2')
matrices=[('u',W('C0')),('A01',W('C0','P01','C0')),('A02',W('C0','P02','C0')),('K',K),('Ka',W('K','a')),('Kb',W('K','b'))]
for name,key in [('DA','D_A_on_y'),('DB','D_B_on_x')]:
 for index,t in enumerate(data['residual_words'][key]):matrices.append((name+str(index),W(*t['word'])))
records=[]
for name,matrix in matrices:
 record={'name':name,**describe(matrix)}
 for label,rep,expected in [('C2',C2,name=='DA0'),('C1',C1,name=='DB0'),('K',K,name in ('K','Ka','Kb'))]:
  actual=describe(v.mm(matrix,v.adjoint(rep)))['fourth_root_monomial']
  if actual!=expected:raise ValueError((name,label,actual,expected))
  record['left_coset_'+label]=actual
 records.append(record)
result={'status':'PASS','arithmetic':'exact Gaussian Fraction pairs','words_sha256':hashlib.sha256(a.words.read_bytes()).hexdigest(),'arithmetic_sha256':ARITHMETIC_SHA,'records':records,'scope':'Coset memberships for the four-coordinate proof in ENDPOINT-OBSTRUCTION.md, with the full finite fourth-root monomial group as an allowed enlargement of the actual free group.'}
if a.out:a.out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','coset_checks':len(records)*3}),flush=True)
