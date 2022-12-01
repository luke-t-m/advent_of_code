import Data.Char
import Data.List
import Data.List.Split
import Data.Maybe

data SnailNo = No Int | Pair (SnailNo) (SnailNo) deriving (Show,Eq)


parseSN ('[' : a) = Pair (parseSN b) (parseSN c)
 where (b,',':c) = splitl a 0 0
       splitl x p n | x!!p == ',' && n == 0 = splitAt p x
                    | x!!p == '[' = splitl x (p+1) (n+1)
                    | x!!p == ']' = splitl x (p+1) (n-1)
                    | otherwise = splitl x (p+1) n
parseSN x = No (read (filter isDigit x))

{-
smap f (Pair a b) = Pair (smap f a) (smap f b)
smap f (No a) = No (f a)


reduce (Pair (No a) (Pair (No b) (No c))) 4 = reduce (Pair (No (a+b)) (No 0)) 0
reduce (Pair (Pair (No a) (No b)) (No c)) 4 = reduce (Pair (No 0) (No (b+c))) 0



explodeLQ (Pair (No a) (No b)) 4 = a
explodeLQ (Pair (No a) _) _ = 0
explodeLQ (Pair a b) d | explodeLQ a (d+1) /= 0 = explodeLQ a (d+1)
                       | otherwise = explodeLQ b (d+1)


reduce (No x) n | x >= 10 = reduce (Pair (No (x `div` 2)) (No ((x `div` 2)+1))) (n+1)
                | otherwise = (No x)
reduce (Pair a b) n | n == 4 = explode 
                    | otherwise = Pair (reduce a (n+1)) (reduce b (n+1))



explodeM (Pair (No a) (Pair (No b) (No c))) 4 = Pair (No (a+b)) (No (c*100))
explodeM (Pair (Pair (No a) (No b)) (No c)) 4 = Pair (No (a*100)) (No (b+c))
explodeM (Pair a b) d | (explodeM a (d+1)) /= a = Pair (explodeM a (d+1)) b
                     | otherwise = Pair a (explodeM b (d+1))
explodeM x _ = x


findEM (Pair a b) = (findEM a) + (findEM b)
findEM (No a) | a >= 100 = a `div` 100
              | otherwise = 0

explodeL (Pair a b) n | n /= 0 &&   Pair a (explodeL b n)
                      | f /= 0 && (explodeL b f) == b = Pair (explodeL a f) b
                      | otherwise = Pair a (explodeL b 0)
 where f = findEM b
explodeL (No a) n | a >= 100 = No a
                  | otherwise = No (a+n)

explodeR (Pair a b) n | n /= 0 = Pair (explodeR a n) b
                      | f /= 0 && (explodeR a f) == a = Pair a (explodeR b f)
                      | otherwise = Pair (explodeR a 0) b
 where f = findEM a
explodeR (No a) n | a >= 100 = No a
                  | otherwise = No (a+n)



explodeM (Pair (No a) (No b)) 4 = Pair (No (a*100)) (No (b*100))
explodeM (Pair a b) d | (explodeM a (d+1)) /= a = Pair (explodeM a (d+1)) b
                     | otherwise = Pair a (explodeM b (d+1))
explodeM x _ = x


findEML (Pair (No a) (No b)) | a >= 100 = a `div` 100
                             | otherwise = 0
findEML (Pair a b) = (findEML a) + (findEML b)
findEML x = 0

findEMR (Pair (No a) (No b)) | b >= 100 = b `div` 100
                             | otherwise = 0
findEMR (Pair a b) = (findEMR a) + (findEMR b)
findEMR x = 0

lwn (Pair a b) = lwn a
lwn (No a) | a >= 100 = False
           | otherwise = True

rwn (Pair a b) = rwn b
rwn (No a) | a >= 100 = False
           | otherwise = True

--explodeL (Pair (No a) (No b)) n | b >= 100 = Pair (No a) (No b)
--                                | otherwise = Pair (No a) (No (b+n))
explodeL (Pair a b) n -- | (findEML b) == 0 = Pair (explodeL a f) b 
                --      | (findEML b) /= 0 = Pair (explodeL a f) b 
                      | f == 0 && lwn b = Pair a (explodeL b f)
                      | otherwise = Pair (explodeL a f) b 
 where f = max n (findEML b)
explodeL (No a) n | a >= 100 = No a
                  | otherwise = No (a+n)

--explodeR (Pair (No a) (No b)) n | a >= 100 = Pair (No a) (No b)
--                                | otherwise = Pair (No (a+n)) (No b)
explodeR (Pair a b) n -- | (findEML a) == 0  = Pair a (explodeR b f)
                --      | (findEMR a) == 0 = Pair a (explodeR b f)
                      | rwn a = Pair (explodeR a f) b
                      | otherwise = Pair a (explodeR b f)
 where f = max n (findEMR a)
explodeR (No a) n | a >= 100 = No a
                  | otherwise = No (a+n)
-}

explodeM (Pair (No a) (No b)) 4 = Pair (No (a*100)) (No (b*100))
explodeM (Pair a b) d | (explodeM a (d+1)) /= a = Pair (explodeM a (d+1)) b
                     | otherwise = Pair a (explodeM b (d+1))
explodeM x _ = x

explodeL (Pair a b)

gor (Pair a b) | gor a == 

fixEM x@(Pair (No a) (No b)) | a >= 100 = No 0
                             | otherwise = x
fixEM (Pair a b) = Pair (fixEM a) (fixEM b)
fixEM (No a) = (No a)

explode a = fixEM (explodeR (explodeL (explodeM a 0) 0) 0)

split' (Pair a b) | split' a /= a = Pair (split' a) b
                  | otherwise = Pair a (split' b)
split' (No a) | a >= 10 = Pair (No h) (No (h+1))
              | otherwise = No a
 where h = a `div` 2

reduce a | explode a /= a = reduce (explode a)
         | split' a /= a = reduce (split' a)
         | otherwise = a

add a b = reduce (Pair a b)

addAll x = foldl add (head x) (tail x) 


main :: IO ()
main = do
 input <- readFile "example.txt"
 let x = map parseSN (lines input)
 --print x
 print (add (head x) (head (tail x)))
-- print (addAll x)

 putStr "Part 1: "

 putStr "Part 2: "

 print "done."
