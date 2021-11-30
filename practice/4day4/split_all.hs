import Data.List
import Data.List.Split

splitAny l x = filter (/="") (splitAnyW l [x])

splitAnyW [] x = x
splitAnyW (l:ls) x = splitAnyW ls (concat (map (splitOn l) x))
