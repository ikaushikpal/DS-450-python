# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

# Example 1:

# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.


from collections import defaultdict, deque
from typing import List
import heapq


class Twitter:

    def __init__(self):
        self.tweetDb = defaultdict(deque)
        self.followDb = defaultdict(set)
        self.sysClock = 1
        self.MAX_TWEET_ALLOWED = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetDb[userId].appendleft((-self.sysClock, tweetId))
        # making user to follow itself
        self.followDb[userId].add(userId)
        if len(self.tweetDb[userId]) > self.MAX_TWEET_ALLOWED:
            self.tweetDb[userId].pop()
        self.sysClock += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        minHeap = []

        # add latest tweet of all users that user follows to minHeap and itself
        for user in self.followDb[userId]:
            if len(self.tweetDb[user]) > 0:
                record = (self.tweetDb[user][0], 1, user)
                minHeap.append(record)
        heapq.heapify(minHeap)
        
        while len(feed) < 10 and len(minHeap) > 0:
            (_, tweetId), pos, userId = heapq.heappop(minHeap)
            totalTweets = len(self.tweetDb[userId])
            feed.append(tweetId)
            if pos < totalTweets:
                record = (self.tweetDb[userId][pos], pos+1, userId)
                heapq.heappush(minHeap, record)

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followDb[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followDb[followerId]: 
            self.followDb[followerId].remove(followeeId)
# Time Complexity: 
# postTweet - O(1)
# getNewsFeed - O(K + 10logK) = O(K)
# where K is number of user currentUser follows
# follow - O(1)
# unfollow - O(1)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


if __name__ == '__main__':
    sol = Twitter()
    print(sol.postTweet(1, 5))
    print(sol.getNewsFeed(1))
    print(sol.follow(1, 2))
    print(sol.postTweet(2, 6))
    print(sol.getNewsFeed(1))
    print(sol.unfollow(1, 2))
    print(sol.getNewsFeed(1))
