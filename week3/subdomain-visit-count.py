class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subDomains = {}
        cpd = []
        for i in range(len(cpdomains)):
            visits, url = cpdomains[i].split()
            url = url.split(".")
            for i in range(len(url)):
                subDomains[".".join(url[i:])] = subDomains.get(".".join(url[i:]), 0) + int(visits)
        for k,v in subDomains.items():
            cpd.append(f"{v} {k}")
        return cpd