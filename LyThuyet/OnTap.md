# Chapter 1: Introdution
- > What Is AI?
    - Objective of AI is build intelligent entities.
    - View of AI (quan điểm của AI) fall into 4 categories: 
        + Acting Humanly.
        + Thinking Humanly.
        + Thinking Rationally.
        + Acting Rationally.
- > Acting Humanly (Turning Test):
    - Human do not realize (nhận ra) whether they are communicating (giao tiếp) with a human or a AI. 
    - Components of AI: 
        + Natural language processing. 
        + Knowledge representation (biểu diễn): store what it knows or hears (nghe).
        + Automated reasoning (lập luận). 
        + Machine learning.
    - Problems: Not reproducible (tái tạo), constructive (xây dựng &rarr; AI), mathematical analysis. 
- > Thinking Humanly: The Cognitive (nhận thức) modeling approach (tiếp cận).
    - Program's behavior matches human behavior &rarr; program's machanisms could also be operating in humans. 
    - "General Problem Solver" compares the trace of its reasoning steps to that of human subjects in solving the same problems. 
    - Computer models from AI + techniques from psychology (tâm lý học) &rarr; theories (lý thuyết) - human mind. 
    - Cognitive science (Khoa học nhận thức) are now distinct (khác) from AI. 
- > Thinking Rationally: The "Laws (Luật) of thought" approach.
    - Create Intelligent systems by logic programming. 
    - notations (ký hiệu), rules. 
    - Progams could solve any problem described in logical notation.
    - Problems: Not Easy to represent real-world knowledge (biểu diễn tri thức đời thực) using logic.
                Difference between theory and reality (thực tế). 
- > Acting Rationally: The rational agent approach
    - Rational behavior: doing the right thing.
    - The right thing: maximize goal achievement (tối đa hóa mục tiêu đạt được).
    - An agent (tác nhân) is an entity that perceives (nhận thức) and acts.
    - This course is about designing rational agents.
    - Advantages (Thuận lợi):  
        - It is more general (tổng quát) than the “laws of thought” approach.
        - It is easily extendable (mở rộng) with more scientific methodologies (phương pháp luận).
- > The main topics in AI
    - Search (includes Game Playing).
    - Representing Knowledge and Reasoning with it.
    - Planing.
    - Learning.
    - Natural Language processing.
    - Expert Systems.
    - Interacting with the Environment (Ex: Vision (thị giác), Speech recognition (Nhận dạng giọng nói), Robotics,...).
# Chapter 2: Intelligent Agents
- > Agents and Environments: 
    - Perceives (nhận thức) its environment through sensors (cảm biến). 
    - acts upon that environment through actuators.
        ![alt text](image.png)
    - Agent's percept: The agent's inputs at any given instant (Nhận input ở bất kỳ thời điểm nào).
    - Agent's percept sequence: The complete history of everything that the agent has perceived (Toàn bộ lịch sử thông tin đã cảm nhận). 
    - Agent's behavior (~agent function): maps any percept sequence to an action. 
    - Agent's program: the concrete implementation (thực hiện cụ thể) of the agent action. 
        > Example:
        ![alt text](image-1.png)
- > The Concept (khái niệm) Of Rationality: 
    - A Rational agent choose the action that maximizes the expected value of the performance (hiệu suất) measure given the percept sequence. 
- > The nature (bản chất) Of Environments. 
    - Specifying (xác định) task environment
        ![alt text](image-2.png)
        ![alt text](image-3.png)
    - Properties of task environments
        - 1: 
            - Fully observable. 
            - Partially observable. 
            - Unobservable. 
        - 2:
            - Single agent: solving a crossword puzzle.
            - Multiagent: 
                - Competitive (cạnh tranh): chess. 
                - Cooperative (hợp tác): Taxi-driving.
        - 3: 
            - Deterministic (xác định): if the next state of the environment is completely determined by the current state and the action executed by the agent.
            - Stochastic (ngẫu nhiên). 
        - 4: 
            - Episodic (từng đợi).  
            - Sequential (tuần tự): The current decision(quyết định) could affect(ảnh hưởng) all future decision; e.g., chess and taxi-driving. 
        - 5: 
            - Dynamic: environment can change (e.g., taxi-driving).
            - Static: Otherwise. 
            - Semi-dynamic: (e.g., chess: score).
        - 6: Discrete vs. continuous - applies to the state of the environment, to the way time is handled, percepts and actions of the agent. 
            - The chess environment has a finite (hữu hạn) number of distinct states, a discrete set of percepts and actions. 
            - Taxi-driving is a continuous-time and continuous-state. 
        - 7: Known vs. unknown - In a know environment, the outcomes for all actions are given.
- > The Structure Of Agents
    - AGENT = ARCHITECTURE + PROGRAM.
    - Agent Programs: 
        - They take the current percepts as input and return an action.
        - Four basic types: 
            ++ Simple reflex agents ++
            ++ Reflex agents with state ++
            ++ Goal-based agents ++
            ++ Utility-based agents ++
        - >> Simple reflex agents
            ![alt text](image-4.png)
            E.g., Robot Vacuum: Dirty &rarr; Suck.
        - >> Model-based reflex agents
            Internal state (trạng thái cục bộ) &rarr; Track (theo dõi) Aspects (nhiều khía cạnh).
            Not current percept.
            ![alt text](image-5.png)
            E.g., Robot Vacuum: Remember dirty locations &rarr; Return to suck. 
        - >> Goal-based agents: 
            Needs some sort of goal information (1 vài thông tin mục tiêu).
            Combines the goal information with model &rarr; right actions. 
            ![alt text](image-6.png) 
            E.g., Robot Vacuum: Plan to clean the entire (toàn bộ) room (remember&avoid obstacle).
        - >> Utility-based agent: 
            Unhappy # Happy.
            Score exactly how happy. 
            Utility Function. 
            ![alt text](image-7.png)
            E.g., Robot vacuum: 
                The Utility function can be designed to evaluate (đánh giá): 
                    How clean the room is (%).
                    The energy consumption (sự tiêu thụ) of the robot. 
                    The priority of dirty areas. 
                    The optimal (tối ưu) time to complete the task.
        - >> Learning agents
            Improve: cải thiện. 
            Determines: xác định. 
            Decides: quyết định. 
            ![alt text](image-8.png)
# Chapter 3: Solving problems by searching
- > Breadth first search (BFS).
- > Depth First Search (DFS).
- > Depth Limited Search (DLS).
- > Iterative deepening depth-first search (IDDFS).
# Chapter 4: Informed search and exploration
- > Greedy Best-First-Search.
- > A*.
- > ... sáng 31/03/2025
# Chapter 5: Logical Agent
- ![alt text](image-9.png)
- Operator precedence: not, and, or, => <=>
- ![alt text](image-10.png)
- A sentence is valid if it is true in all models. 
- A sentence is satisfiability if it is true in some models.
- ![alt text](image-11.png)
    + P: Pit.
    + B: Wind. 
- Conjunctive (liên hợp) Normal Form (CNF)
    ![alt text](image-12.png)
- ![alt text](image-13.png)
- ![alt text](image-14.png)
# Chapter 6: First Order Logic
- First Order Logic
    - Basic symbols: 
        - Constant symbols &rarr; objects. EX: Alice, Pop,...
        - Predicate symbols &rarr; relations. Ex: Loves(Alice, Pop)...
        - Function symbols &rarr; Functional Relations. FatherOf(Bob)...
    - Basic Elements: 
        - Constants: KingJohn, 2, UCB,...
        - Variables: x, y, a, b,...
        - Predicate (Relations): Brother, >,...
        - Functions: LeftLeg, Mother,...
        - Connectives: ![alt text](image-15.png)
        - Quantifiers: ![alt text](image-16.png)
    - Using First Order Logic: 
        - TELL.
        - ASK.
        - SUBST.
        - ![alt text](image-17.png)
        ![alt text](image-18.png)
        - Unification (hợp nhất): ![alt text](image-19.png)
    - ![alt text](image-20.png)
    - ![alt text](image-21.png)
    ![alt text](image-22.png)
    3. ![alt text](image-23.png)
    4. ![alt text](image-24.png)
    5. ![alt text](image-25.png)
    5. ![alt text](image-26.png)
# Chapter 7: Quantifying Uncertainty
- Boolean. Cavity(có sâu răng không) &rarr; True or False. 
- Discrete Random Variables: Weather thuộc {sunny, rain, cloudy, snow}
- Continuous Random Variables: First: Temp = 21.6°C, Second: 21.6234°C, Third: 21.62345678°C. 
- ![alt text](image-27.png)
- ![alt text](image-28.png)
- ![alt text](image-29.png)
- ![alt text](image-30.png)
- ![alt text](image-31.png)
- ![alt text](image-32.png)
- Independence (độc lập): 
    ![alt text](image-33.png)
- Conditional indenpence:
    ![alt text](image-34.png)
- Conditional indecpence contd: 
    ![alt text](image-35.png)
- Bayes' Rule and It Use
    ![alt text](image-36.png)
    ![alt text](image-37.png)
    ![alt text](image-38.png)