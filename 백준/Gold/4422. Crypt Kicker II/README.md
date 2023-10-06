# [Gold IV] Crypt Kicker II - 4422 

[문제 링크](https://www.acmicpc.net/problem/4422) 

### 성능 요약

메모리: 115004 KB, 시간: 136 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 문자열

### 문제 설명

<p>A common but insecure method of encrypting text is to permute the letters of the alphabet. That is, in the text, each letter of the alphabet is consistently replaced by some other letter. So as to ensure that the encryption is reversible, no two letters are replaced by the same letter.</p>

<p>A common method of cryptanalysis is the known plaintext attack. In a known plaintext attack, the cryptanalist manages to have a known phrase or sentence encrypted by the enemy, and by observing the encrypted text then deduces the method of encoding.</p>

<p>Your task is to decrypt several encrypted lines of text, assuming that each line uses the same set of replacements, and that one of the lines of input is the encrypted form of the plaintext</p>

<pre>the quick brown fox jumps over the lazy dog</pre>

### 입력 

 <p>The encrypted lines contain only lower case letters and spaces and do not exceed 80 characters in length. There are at most 100 input lines.</p>

### 출력 

 <p>The input consists of several lines of input. Each line is encrypted as described above. Decrypt each line and print it to standard output. If there is more than one possible decryption, any one will do. If decryption is impossible, output a single line:</p>

<pre>No solution.</pre>

