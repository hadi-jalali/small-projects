%%%%% Grammar

s(s(NP,VP)) --> np(Number,Person,subject,inanimate,mo,NP), vp(Number,Person,inanimate,VP).
s(s(NP,VP)) --> np(Number,Person,subject,animate,mo,NP), vp(Number,Person,_,VP).
np(Number,3,_,Animacy,mo,np(Det,Nbar)) --> det(Number,Det), nbar(Number,Animacy,Nbar).
np(Number,3,_,Animacy,mo,np(Det,Nbar,PP)) --> det(Number,Det), nbar(Number,Animacy,Nbar),pp(_,_,PP). 
np(Number,3,object,_,lone,np(PP)) --> pp(Number,_,PP).
np(Number,Person,X,animate,mo,np(Pro)) --> pro(Number,Person,X,Pro). 
nbar(Number,Animacy,nbar(N)) --> n(Number,Animacy,N).
nbar(Number,Animacy,nbar(JP)) --> jp(Number,Animacy,JP).
jp(Number,Animacy,jp(Adj,JP)) --> adj(Adj),jp(Number,Animacy,JP).
jp(Number,Animacy,jp(Adj,N)) --> adj(Adj), n(Number,Animacy,N).
vp(Number,Person,Animacy,vp(V,NP)) --> v(tv,Number,Person,Animacy,V), np(_,_,object,_,_,NP). 
vp(Number,Person,Animacy,vp(V)) --> v(iv,Number,Person,Animacy,V). 
vp(Number,Person,Animacy,vp(V,NP)) --> v(iv,Number,Person,Animacy,V),np(_,_,_,_,lone,NP).
pp(Number,Animacy,pp(Prep,NP)) --> prep(Prep), np(Number,_,_,Animacy,mo,NP).


prep(prep(Word)) --> [Word], {lex(Word,prep)}.
adj(adj(Word)) --> [Word], {lex(Word,adj)}.
pro(Number,Person,X,pro(Word)) --> [Word], {lex(Word,pro,Number,Person,X)}. 
det(Number,det(Word)) --> [Word], {lex(Word,det, Number)}. 
n(Number,Animacy,n(Word)) --> [Word], {lex(Word,n,Number,Animacy)}. 
v(Transitivity,Number,Person,Animacy,v(Word)) --> [Word], {lex(Word,Transitivity,Number,Person,Animacy)}. 

%%%%% Lexicon

% Pronouns
lex(i,pro,singular,1,subject).
lex(you,pro,singular,2,subject).
lex(he,pro,singular,3,subject).
lex(she,pro,singular,3,subject).
lex(it,pro,singular,3,subject).
lex(we,pro,plural,1,subject).
lex(you,pro,plural,2,subject).
lex(they,pro,plural,3,subject).
lex(me,pro,singular,1,object).
lex(you,pro,singular,2,object).
lex(him,pro,singular,3,object).
lex(her,pro,singular,3,object).
lex(it,pro,singular,3,object).
lex(us,pro,plural,1,object).
lex(you,pro,plural,2,object).
lex(them,pro,plural,3,object).

% Verbs
lex(know,tv,singular,1,animate).
lex(know,tv,singular,2,animate).
lex(knows,tv,singular,3,animate).
lex(know,tv,plural,_,animate).
lex(see,tv,singular,1,animate).
lex(see,tv,singular,2,animate).
lex(sees,tv,singular,3,animate).
lex(see,tv,plural,_,animate).
lex(hire,tv,singular,1,animate).
lex(hire,tv,singular,2,animate).
lex(hires,tv,singular,3,animate).
lex(hire,tv,plural,_,animate).
lex(fall,iv,singular,1,inanimate).
lex(fall,iv,singular,2,inanimate).
lex(falls,iv,singular,3,inanimate).
lex(fall,iv,plural,_,inanimate).
lex(sleep,iv,singular,1,animate).
lex(sleep,iv,singular,2,animate).
lex(sleeps,iv,singular,3,animate).
lex(sleep,iv,plural,_,animate).

% Determiners
lex(the,det,_).
lex(a,det,singular).
lex(two,det,plural).

% Nouns
lex(man,n,singular,animate).
lex(woman,n,singular,animate).
lex(apple,n,singular,inanimate).
lex(chair,n,singular,inanimate).
lex(room,n,singular,inanimate).
lex(men,n,plural,animate).
lex(women,n,plural,animate).
lex(apples,n,plural,inanimate).
lex(chairs,n,plural,inanimate).
lex(rooms,n,plural,inanimate).

% Prepositions
lex(on,prep).
lex(in,prep).
lex(under,prep).

% Adjectives
lex(old,adj).
lex(young,adj).
lex(red,adj).
lex(short,adj).
lex(tall,adj).

%%%% Queries

% s(Tree,[the,woman,sees,the,apples],[]).
% Tree = s(np(det(the), nbar(n(woman))), vp(v(sees), np(det(the), nbar(n(apples)))))

% s(Tree,[a,woman,knows,him],[]).
% Tree = s(np(det(a), nbar(n(woman))), vp(v(knows), np(pro(him))))

% s(Tree,[two,woman,hires,a,man],[]).
% false

% s(Tree,[two,women,hire,a,man],[]).
% Tree = s(np(det(two), nbar(n(women))), vp(v(hire), np(det(a), nbar(n(man)))))

% s(Tree,[she,knows,her],[]).
% Tree = s(np(pro(she)), vp(v(knows), np(pro(her))))

% s(Tree,[she,know,the,man],[]).
% false

% s(Tree,[us,see,the,apple],[]).
% false

% s(Tree,[we,see,the,apple],[]).
% Tree = s(np(pro(we)), vp(v(see), np(det(the), nbar(n(apple)))))

% s(Tree,[i,know,a,short,man],[]).
% Tree = s(np(pro(i)), vp(v(know), np(det(a), nbar(jp(adj(short), n(man))))))

% s(Tree,[he,hires,they],[]).
% false

% s(Tree,[two,apples,fall],[]).
% Tree = s(np(det(two), nbar(n(apples))), vp(v(fall)))

% s(Tree,[the,apple,falls],[]).
% Tree = s(np(det(the), nbar(n(apple))), vp(v(falls)))

% s(Tree,[the,apples,fall],[]).
% Tree = s(np(det(the), nbar(n(apples))), vp(v(fall)))

% s(Tree,[i,sleep],[]).
% Tree = s(np(pro(i)), vp(v(sleep)))

% s(Tree,[you,sleep],[]).
% Tree = s(np(pro(you)), vp(v(sleep))) ;
% Tree = s(np(pro(you)), vp(v(sleep))) ;

% s(Tree,[she,sleeps],[]).
% Tree = s(np(pro(she)), vp(v(sleeps)))

% s(Tree,[he,sleep],[]).
% false

% s(Tree,[them,sleep],[]).
% false

% s(Tree,[a,men,sleep],[]).
% false

% s(Tree,[the,tall,woman,sees,the,red],[]).
% false

% s(Tree,[the,young,tall,man,knows,the,old,short,woman],[]).
% Tree = s(np(det(the), nbar(jp(adj(young), jp(adj(tall), n(man))))),
%	 vp(v(knows), np(det(the), nbar(jp(adj(old), jp(adj(short), n(woman)))))))

% s(Tree,[a,man,tall,knows,the,short,woman],[]).
% false

% s(Tree,[a,man,on,a,chair,sees,a,woman,in,a,room],[]).
% Tree = s(np(det(a), nbar(n(man)), pp(prep(on), np(det(a), 
% nbar(n(chair))))), vp(v(sees), np(det(a), nbar(n(woman)), 
% pp(prep(in), np(det(a), nbar(n(room)))))))

% s(Tree,[a,man,on,a,chair,sees,a,woman,a,room,in],[]).
% false

% s(Tree,[the,tall,young,woman,in,a,room,on,the,chair,in,a,room,in,the,room,sees,the,red,apples,under,the,chair],[]).
% Tree = s(np(det(the), nbar(jp(adj(tall), jp(adj(young), n(woman)))), 
% pp(prep(in), np(det(a), nbar(n(room)), pp(prep(on), np(det(the), 
% nbar(n(chair)), pp(prep(in), np(det(a), nbar(n(room)), pp(prep(in), 
% np(det(the), nbar(n(room))))))))))), vp(v(sees), np(det(the), 
% nbar(jp(adj(red), n(apples))), pp(prep(under), np(det(the), nbar(n(chair)))))))

% Queries for animacy

% s(Tree,[the,woman,sees,the,apples],[]).
% Tree = s(np(det(the), nbar(n(woman))), vp(v(sees), np(det(the), nbar(n(apples)))))

% s(Tree,[a,woman,knows,him],[]).
% Tree = s(np(det(a), nbar(n(woman))), vp(v(knows), np(pro(him))))

% s(Tree,[the,man,sleeps],[]).
% Tree = s(np(det(the), nbar(n(man))), vp(v(sleeps)))

% s(Tree,[the,room,sleeps],[]).
% false

% s(Tree,[the,apple,sees,the,chair],[]).
% false

% s(Tree,[the,room,knows,the,man],[]).
% false

% s(Tree,[the,apple,falls],[]).
% Tree = s(np(det(the), nbar(n(apple))), vp(v(falls)))

% s(Tree,[the,man,falls],[]).
% Tree = s(np(det(the), nbar(n(man))), vp(v(falls)))


%%%% Discussion

% Starting the project, my aim was to develop a grammar that includes many aspects
% of the english language. However, the base program which passed all the opposed tests
% in the document were not enough. This program failed to recognize sentences that had prepositional
% phrases right after verbs (with no object) so a third np rule was made that only contained pp. With this 
% the grammar accepted sentences like "the apple falls on the chair" unlike before. But with the introduction
% of the latest np rule, this meant that the grammar was accepting two preposition right after each other 
% for example "the man on on the chair" would pass through this grammar but is not grammatically correct. In order
% to fix this proble a final variable was added to the np clauses . Using the extra variable, the last np rule was seperated
% from the other rules and was only called inside an objective noun phrase. The np called in the pp rule could not take
% the last np rule which lead to the correct form of prepositional phrases. Howeever, this still was not perfect because the grammar accepted
% wrong sentences like "the man falls the man" hence the vp rule was divided into more sections which made sure that a intransitive verb
% only accepted prepositional phrases for the second part of the sentence