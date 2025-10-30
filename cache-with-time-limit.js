var TimeLimitedCache = function() {
    this.cache = [];
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration)
{
    const time = Date.now();
    const sortedTemp = this.cache.filter(item => item[0] === key);
    const temp = sortedTemp[0];

    if (sortedTemp.length < 1)
    {
        const data = {index: this.cache[this.cache.length-1].index + 1, value, expiration: time + duration};
        this.cache.push([key, data]);
        return false;
    }
    if (temp[1].expiration > time)
    {
        const data = {index: this.cache[this.cache.length-1].index + 1, value, expiration: time + duration};
        this.cache = this.cache.toSpliced(temp[1].index, 1, [key, data]);
        return true;
    }
    return false;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key)
{
    const sortedTemp = this.cache.filter(item => item[0] === key);
    const temp = sortedTemp[0];
    console.log(key, temp);
    if (sortedTemp.length < 1)
        return -1;
    if (temp[1].expiration < Date.now())
        return -1;
    return temp[1].value;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function()
{
    const time = Date.now();
    const sortedTemp = this.cache.filter(item => item[1].expiration > time);
    return sortedTemp.length;
};


const timeLimitedCache = new TimeLimitedCache();
timeLimitedCache.set(1, 42, 1000); // false
timeLimitedCache.set(3, 42, -1000); // false
timeLimitedCache.get(1) // 42
const ress = timeLimitedCache.count() // 1

console.log(ress);


