# Naxos-AKE
Implementation of Authenticated Key Exchange protocol called Naxos. Based on the publication "Stronger Security of Authenticated Key Exchange".

In order to simulate the operation of the protocol, the following mathematical operations had to be performed:

![image](https://user-images.githubusercontent.com/90600068/207359834-dbe718e9-96ef-4734-8f68-8f5cba6369c2.png)


At the beginning, it was necessary to form a cyclic group p and q, where p=2*q+1, then a generator g from the interval 1 < g < p-1 had to be created, for the sake of speed of calculations I assumed g = 2. Then I created a group G, whose elements are g^ and mod p. The private, public and ephemeral keys of parties A and B had to be generated in turn. Next, I follow the assumptions from the publication and create session keys A and B and finally check whether these keys are the same.

ref. https://www.researchgate.net/publication/221106180_Stronger_Security_of_Authenticated_Key_Exchange
