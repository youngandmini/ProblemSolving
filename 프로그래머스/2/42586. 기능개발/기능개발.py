def solution(progresses, speeds):
    
    deployments = []
    
    for i in range(len(progresses)):
        rest = 100 - progresses[i]
        time = rest // speeds[i]
        if rest%speeds[i] != 0:
            time += 1
        deployments.append(time)
        
    print(deployments)
    
    # 이전보다 숫자가 작아지면 이전과 함께 배포
    # 이전보다 숫자가 커지면 앞쪽꺼 먼저 배포
    answer = []
    max_time = deployments[0]
    count = 1
    for i in range(1, len(deployments)):
        if max_time < deployments[i]:
            answer.append(count)
            count = 1
            max_time = deployments[i]
        else:
            count += 1
    answer.append(count)

    return answer