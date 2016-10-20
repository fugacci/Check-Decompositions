# Splitting Algorithms
Macaulay2 code of algorithms for checking the splittability of a simplicial complex with respect to a given field.

####Homological Splitting Algorithm 
***

The following code allows checking if a standard decomposition of a simplicial complex is a homological splitting with respect to a given field:

```
loadPackage "SimplicialComplexes";
isHomologicalSplitting=(T,T1,T2)->(
if T1=={} or T2=={} then return true;
A=simplicialComplex(T);
A1=simplicialComplex(T1);
A2=simplicialComplex(T2);
B=0;
C=monomialIdeal(A1)+monomialIdeal(A2);
if dual(C)==ideal(product(gens R)) then return true;
G=simplicialComplex(C);
for k from 0 to dim(A) do (
if rank(homology(k,A))==rank(homology(k,A1))+rank(homology(k,A2))+rank(homology(k-1,G)) then B=B+1
); if B==dim(A)+1 then return true else return false;);
```

####Betti Splitting Algorithm 
***

The following code allows checking if a standard decomposition of a simplicial complex is a Betti splitting with respect to a given field:

```
loadPackage "SimplicialComplexes";
isBettiSplitting=(L,L1,L2)->(
T=L; T1=L1; T2=L2;
if not isHomologicalSplitting(T,T1,T2) then return false;
D=simplicialComplex(L);
D1=simplicialComplex(L1);
D2=simplicialComplex(L2);
F=monomialIdeal(D1)+monomialIdeal(D2);
J=simplicialComplex(F);
N=0;
H=0;
for k from 0 to dim(J) do (
M=flatten entries faces(k,J); H=(#M)+H; for j from 0 to #M-1 do (
T=flatten entries facets(link(D,M_j));
T1=flatten entries facets(link(D1,M_j));
T2=flatten entries facets(link(D2,M_j));
if not isHomologicalSplitting(T,T1,T2) then return false else N=N+1;
);); if N==H then return true);
```

####Betti Splitting Probability 
***

The following code allows computing the Betti splitting probability for a simplicial complex with respect to a given field:

```
loadPackage "SimplicialComplexes";
BettiSplittingProbability=(L)->(
N=0;
for k from 1 to floor(#L/2) do (S=subsets(L,k);
for j from 0 to #S-1 do (L1=S_j; L2=toList(set(L)-set(L1)); 
if isBettiSplitting(L,L1,L2) then N=N+1);
P=N/(2^(#L-1)-1););
return P);
```

####Attribution
***

If you use our package in your project we encourage you to cite our work.
Please use the following reference:

```
  @article{SpittingForManifolds,
    author       = {D. Bolognini, U. Fugacci},
    title        = {Betti splitting from a topological point of view},
    month        = {September},
    year         = {2016}
  }
```
