#!/usr/bin/env python3
"""Exact inherited native phases for the opposite-orientation Laurent border.
Apache-2.0; Yiyang (@Lyy-iiis), substantial OpenAI Codex assistance.
Uses an explicitly hashed local arithmetic/source-reader dependency.
"""
import argparse,json,sys,types
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ARITHMETIC_PIN='119d89830ebc28ba66bdff8a4fbeaa18a3a5d746f9f70d32652cd067e72077ea'
ENGINE_PIN='2982ead07721e83358dc67c6f49c2b4c16a236a6bebdfd72f58221be1f5d0962'
def load(path,name):
 raw=path.read_bytes();mod=types.ModuleType(name);mod.__file__=str(path);sys.modules[name]=mod;exec(compile(raw,str(path),'exec'),mod.__dict__);return mod,sha256(raw).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--arithmetic',type=Path,default=HERE/'vendor/check_border_native_matrices.py');ap.add_argument('--engine',type=Path,default=HERE/'vendor/clifford_exact.py');ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
 if a.out.exists():raise ValueError('Fresh output')
 if sha256(a.arithmetic.read_bytes()).hexdigest()!=ARITHMETIC_PIN:raise ValueError('Exact arithmetic source pin')
 if sha256(a.engine.read_bytes()).hexdigest()!=ENGINE_PIN:raise ValueError('Inherited exact phase source pin')
 x,ah=load(a.arithmetic,'laurent_border_matrix_arithmetic');x.need(x.PIN==ENGINE_PIN,'Arithmetic and engine pins agree');ce,_=load(a.engine,'laurent_actual_clifford')
 rows=[];controls=[]
 for f in (1,2,3):
  q=x.actual(ce.fourier(f));qi=x.adj(q);n=1<<f;I=x.eye(n);Z=x.zero(n)
  x.need(x.mm(q,qi)==I,'Exact actual inverse, not a substituted parity surrogate')
  U=x.block(I,q,Z,I);L=x.block(I,Z,x.scale(qi,-1),I);B=x.scalar_block(1,-1,1,0,n)
  for eps in (F(1,2),F(1,4)):
   S=x.scalar_block(1,0,0,eps,n);Si=x.scalar_block(1,0,0,1/eps,n)
   out=x.mm(x.mm(x.mm(x.mm(S,U),L),B),Si)
   residual=x.scale(x.add(I,qi,-1),eps);wanted=x.block(q,Z,residual,qi)
   x.need(out==wanted,'Actual absolute-phase Laurent endpoint')
   J=x.scalar_block(0,1,-1,0,n);Ji=x.scale(J,-1)
   # Transpose is literal, WITHOUT conjugating complex coefficients.
   tr=[list(r) for r in zip(*out)];candidate_inverse=x.mm(x.mm(J,tr),Ji)
   x.need(x.mm(out,candidate_inverse)==x.eye(2*n) and x.mm(candidate_inverse,out)==x.eye(2*n),'Actual transpose/signed-swap adjugate gives exact inverse')
   false_exact=x.block(q,Z,Z,qi)
   x.need(out!=false_exact,'Positive-epsilon residual cannot be declared zero')
   controls.append({'fiber_width':f,'epsilon':str(eps),'false_exact_endpoint_rejected':True})
   # Fresh D1D2 commute with both Q directions; include their actual phases.
   D=x.actual(ce.fourier(2));jointp=x.kron(D,q);jointm=x.kron(D,qi)
   physical=x.block(jointp,x.zero(4*n),x.kron(D,residual),jointm)
   rows.append({'fiber_width':f,'epsilon':str(eps),'physical_pair_dimension':8*n,'physical_matrix_sha256':x.digest_matrix(physical),'coherent_inverse_via_actual_transpose':True})
 r={'status':'PASS_NATIVE_PHASE_LAURENT_BORDER_AND_COHERENT_INVERSE_NOT_A_BOUND','arithmetic_sha256':ah,'engine_sha256':x.PIN,'rows':rows,'controls':controls,'scope':'Actual canonical source Fourier matrices and opposite Q directions, two distinct fresh D model factors. The transpose/adjugate is a matrix identity, not yet a source-bound whole-native transpose implementation or recursive closure theorem. Helpers, error and precision obligations are not waived.'}
 r['checker_sha256']=sha256(Path(__file__).read_bytes()).hexdigest();a.out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'fixtures':len(rows),'controls':len(controls)}))
if __name__=='__main__':main()
