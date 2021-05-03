from bs4 import BeautifulSoup
import json
import re
html="""
<section id="education-section" class="pv-profile-section education-section ember-view"><header class="pv-profile-section__card-header">
  <h2 class="pv-profile-section__card-heading">
    Education
  </h2>

<!----></header>

  <ul class="pv-profile-section__section-info section-info pv-profile-section__section-info--has-no-more">
      <li id="365017724" class="pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"><div class="display-flex justify-space-between full-width">
  <div class="display-flex flex-column full-width">
<a data-control-name="background_details_school" href="/school/13513/?legacySchoolId=13513" id="ember635" class="ember-view">        <div class="pv-entity__logo">
  <img src="https://media-exp1.licdn.com/dms/image/C510BAQFkGVsBobrK1A/company-logo_100_100/0/1553409868557?e=1628121600&amp;v=beta&amp;t=AoRsXWcvmDtevB881ioaq0lu4kbppz7Nay0Yxa6q0Wc" loading="lazy" alt="Jadavpur University" id="ember637" class="pv-entity__logo-img pv-entity__logo-img EntityPhoto-square-4 lazy-image ember-view">
</div>

<div class="pv-entity__summary-info pv-entity__summary-info--background-section">
  <div class="pv-entity__degree-info">
    <h3 class="pv-entity__school-name t-16 t-black t-bold">Jadavpur University</h3>

      <p class="pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal">
        <span class="visually-hidden">Degree Name</span>
        <span class="pv-entity__comma-item">Bachelor’s Degree</span>
      </p>
      <p class="pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal">
        <span class="visually-hidden">Field Of Study</span>
        <span class="pv-entity__comma-item">Computer Science</span>
      </p>
<!---->  </div>

    <p class="pv-entity__dates t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates attended or expected graduation</span>
      <span>
            <time>2015</time> – <time>2019</time>
      </span>
    </p>

<!----></div>

</a>
<!---->  </div>

<!----></div>
</li>
  </ul>

<!----></section>
"""
#  t=BeautifulSoup(html,'html.parser').find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"})
def clean_string(var):
    var=str(var)
    var=var.strip()
    var=var.replace('\n','')
    return var

# edusect=BeautifulSoup(html,'html.parser').find("section", {"id":"education-section"})
# print(edusect)
i=0
print('hello world')
html_soup = BeautifulSoup(html,'html.parser')
Defaults1 = {'Name':'','Link':'','College': '', 'Degree': '', 'Branch': '', 'duration': '','designation': '', 'company': '','dates_employed': '', 'employ_duration': ''}
ids1 = []
thisdict = dict.fromkeys(ids1, Defaults1)
test =html_soup.find("div",{"class":"pv-profile-section-pager ember-view"})
# test=html_soup.find_element_by_xpath("//*[@id='ember649']/div[2]")
print(test)
if (html_soup.find("li", {"class":"pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"})):
        print('section1')
        # edusect=html_soup.find("section", {"class":"pv-profile-section education-section ember-view"})
        for t in html_soup.find_all("li", {"class": "pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"}):
            # print('university',university)
            # print('branch',branch)
            if(t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).find(text=re.compile("Jadavpur University",re.IGNORECASE))) :
                print('@@univ')
                if (html_soup.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).find(text=re.compile("Computer",re.IGNORECASE))) is not None:
                    thisdict['college']=t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).text if t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}) else ''
                    thisdict['degree']=t.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text if t.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}) else ''
                    # thisdict['branch']=clean_string(t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text) if t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).find(text=re.compile("Computer Science",re.IGNORECASE)) else '',
                    thisdict['branch']=clean_string(t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text) if t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).find(text=re.compile("Computer",re.IGNORECASE)) else ''
                    thisdict['duration']=clean_string(t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"}).find("span",{"class":""}).text) if t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"}).find("span",{"class":""}) else ''
            for x, y in thisdict.items():
                print(x,y)
            # IDs = []
            # Defaults = {}
            # expdict = dict.fromkeys(IDs, Defaults)
            # i=0

#             # if (html_soup.find("section", {"class":"pv-profile-section experience-section ember-view"})):
#             #     print("@@@@here@@@@@")
#             #     for k in html_soup.find_all("div",{"class":"pv-entity__summary-info pv-entity__summary-info--background-section mb2"},limit=2) :
#             #             print("####there@@@@@")
#             #             thisdict['designation']= clean_string(k.find("h3",{"class":"t-16 t-black t-bold"}).text) if k.find("h3",{"class":"t-16 t-black t-bold"}) else ''
#             #             thisdict['company']=clean_string(k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}).text) if k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}) else ''
#             #             thisdict['employ_duration'] =clean_string(k.find("span",{"class":"pv-entity__bullet-item-v2"}).text) if k.find("span",{"class":"pv-entity__bullet-item-v2"}) else ''
#             #             thisdict['dates_employed'] =clean_string(k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"}).find("span",{"class":""}).text) if k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"}) else ''
#             #                             # i=i+1            
#             #     else :
#             #         thisdict=''

#                     # 'Edu':thisdict,

# # else :
# #       thisdict=''
                
# # for x, y in thisdict.items():
# #   print(x, y)