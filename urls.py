def returnUrl(req):
    urls = {
        "nomal":"https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3646&id=kr_010802000000",
        "haksa":"https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3638&id=kr_010801000000",
        "admission":"https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3654&id=kr_010803000000",
        "scholarship":"https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3662&id=kr_010804000000",
        "international":"https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=9457435&id=kr_010807000000",
        "event":"https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=11533472&id=kr_010808000000"}
    return urls[req]
