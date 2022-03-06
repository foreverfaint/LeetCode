package main

import "fmt"

type MyHashMapEntry struct {
	Key int
	Val int
}

type MyHashMapBucket = []MyHashMapEntry

type MyHashMap struct {
	data [1000]MyHashMapBucket
}

func Constructor() MyHashMap {
	return MyHashMap{}
}

func (this *MyHashMap) Put(key int, value int) {
	h := key % cap(this.data)

	bucket := this.data[h]
	if bucket == nil {
		bucket = MyHashMapBucket{}
		this.data[h] = bucket
	}

	for i, e := range bucket {
		if e.Key == key {
			bucket[i] = MyHashMapEntry{key, value}
			return
		}
	}

	this.data[h] = append(bucket, MyHashMapEntry{key, value})
}

func (this *MyHashMap) Get(key int) int {
	h := key % cap(this.data)

	bucket := this.data[h]
	if bucket == nil {
		return -1
	}

	for _, e := range bucket {
		if e.Key == key {
			return e.Val
		}
	}

	return -1
}

func (this *MyHashMap) Remove(key int) {
	h := key % cap(this.data)

	bucket := this.data[h]
	if bucket == nil {
		return
	}

	for i, e := range bucket {
		if e.Key == key {
			this.data[h] = append(bucket[:i], bucket[i+1:]...)
			return
		}
	}
}

func main() {
	m := Constructor()
	m.Put(1, 1)
	m.Put(2, 2)
	fmt.Println(m.Get(1))
	fmt.Println(m.Get(3))
	fmt.Println(m.Get(2))
	m.Put(2, 1)
	fmt.Println(m.Get(2))
	m.Remove(2)
	fmt.Println(m.Get(2))
}
