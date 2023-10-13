# [Gold V] CDVII - 4413 

[문제 링크](https://www.acmicpc.net/problem/4413) 

### 성능 요약

메모리: 2084 KB, 시간: 4 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 파싱, 정렬, 문자열

### 제출 일자

2023년 10월 14일 03:24:30

### 문제 설명

<p>Roman roads are famous for their longevity and sound engineering. Unfortunately, sound engineering does not come cheap, and a number of neo-Caesars have decided to recover the costs through automated tolling.</p>

<p>A particular toll highway, the CDVII, has a fare structure that works as follows: travel on the road costs a certain amount per km travelled, depending on the time of day when the travel begins. Cameras at every entrance and every exit capture the license numbers of all cars entering and leaving. Every calendar month, a bill is sent to the registered owner for each km travelled (at a rate determined by the time of day), plus one dollar per trip, plus a two dollar account charge. Your job is to prepare the bill for one month, given a set of license plate photos.</p>

### 입력 

 <p>Standard input has two parts: the fare structure, and the license photos. The fare structure consists of a line with 24 non-negative integers denoting the toll (cents/km) from 00:00 - 00:59, the toll from 01:00 - 00:59, and so on for each hour in the day. Each photo record consists of the license number of the vehicle (up to 20 alphanumeric characters), the time and date (mm:dd:hh:mm), the word "enter" or "exit", and the location of the entrance or exit (in km from one end of the highway). All dates will be within a single month. Each "enter" record is paired with the chronologically next record for the same vehicle provided it is an "exit" record. "enter" records that are not paired with an "exit" record are ignored, as are "exit" records not paired with an "enter" record. You may assume that no two records for the same vehicle have the same time. Times are recorded using a 24-hour clock. There are not more than 1000 photo records.</p>

### 출력 

 <p>Print a line for each vehicle indicating the license number, and the total bill, in alphabetical order by license number.</p>

