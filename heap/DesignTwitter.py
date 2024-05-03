# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
#
# Implement the Twitter class:
#
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId)
# Composes a new tweet with ID tweetId by the user userId.
# Each call to this function will be made with a unique tweetId.

# List<Integer> getNewsFeed(int userId)
# Retrieves the 10 most recent tweet IDs in the user's news feed.
# Each item in the news feed must be posted by users who the user followed or by the user themself.
# Tweets must be ordered from most recent to least recent.

# void follow(int followerId, int followeeId)
# The user with ID followerId started following the user with ID followeeId.

# void unfollow(int followerId, int followeeId)
# The user with ID followerId started unfollowing the user with ID followeeId.
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.tweets = []  # 每個人貼文
        self.followings = {}
        self.time = 0

    def post_tweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        heapq.heappush(self.tweets, [-self.time, userId, tweetId])

    def get_news_feed(self, userId: int) -> List[int]:
        res = []
        temp = []
        followingSet = self.followings.get(userId, set())
        while self.tweets and len(res) < 10:
            time, user_id, tweetId = heapq.heappop(self.tweets)
            if user_id == userId or user_id in followingSet:
                res.append(tweetId)
            temp.append([time, user_id, tweetId])
        # 加回
        for val in temp:
            heapq.heappush(self.tweets, val)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        followingSet = self.followings.get(followerId, set())
        followingSet.add(followeeId)
        self.followings[followerId] = followingSet

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followings:
            if followeeId in self.followings[followerId]:
                self.followings[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)