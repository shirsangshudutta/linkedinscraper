from bs4 import BeautifulSoup
import json
import re
html_soup="""
<section id="experience-section" class="pv-profile-section experience-section ember-view"><header class="pv-profile-section__card-header">
  <h2 class="pv-profile-section__card-heading">
    Experience
  </h2>

<!----></header>

  <ul class="pv-profile-section__section-info section-info pv-profile-section__section-info--has-no-more">
<li id="ember797" class="pv-entity__position-group-pager pv-profile-section__list-item ember-view">        <section id="ember798" class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
<a data-control-name="background_details_company" href="/company/tata-consultancy-services/" id="ember799" class="full-width ember-view">        <div class="pv-entity__company-details">
  <div class="pv-entity__logo company-logo">
    <img src="https://media-exp1.licdn.com/dms/image/C560BAQHvbHDgKpQwow/company-logo_100_100/0/1606220018212?e=1619654400&amp;v=beta&amp;t=r7Qmw71YFtf3onXeVMmjaA62IXA6f0q5E77BFxmCok0" loading="lazy" alt="Tata Consultancy Services" id="ember801" class="pv-entity__logo-img EntityPhoto-square-5 lazy-image ember-view">
  </div>
  <div class="pv-entity__company-summary-info">
    <h3 class="t-16 t-black t-bold">
      <span class="visually-hidden">Company Name</span>
      <span>Tata Consultancy Services</span>
    </h3>
        <h4 class="t-14 t-black t-normal">
          <span class="visually-hidden">Total Duration</span>
          <span>5 yrs 6 mos</span>
        </h4>
  </div>
</div>
</a>
<!---->  </div>

    <ul class="pv-entity__position-group mt2">
        <li class="pv-entity__position-group-role-item">
          <div id="ember803" class="ember-view"><div class="pv-entity__role-details">
  <span class="pv-entity__timeline-node"></span>
  <div class="display-flex justify-space-between full-width">
    <div class="pv-entity__role-container">
      <div class="pv-entity__role-details-container pv-entity__role-details-container--timeline pv-entity__role-details-container--bottom-margin">

        <div class="pv-entity__summary-info-v2 pv-entity__summary-info--background-section pv-entity__summary-info-margin-top ">
          <h3 class="t-14 t-black t-bold">
            <span class="visually-hidden">Title</span>
            <span>Assitant consultant</span>
          </h3>
<!---->            <div class="display-flex">
              <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
                <span class="visually-hidden">Dates Employed</span>
                <span>2016 – Present</span>
              </h4>
                <h4 class="t-14 t-black--light t-normal">
                  <span class="visually-hidden">Employment Duration</span>
                  <span class="pv-entity__bullet-item-v2">5 yrs</span>
                </h4>
            </div>

            <h4 class="pv-entity__location t-14 t-black--light t-normal block">
              <span class="visually-hidden">Location</span>
              <span>kolkata</span>
            </h4>
<!---->        </div>


<!---->      </div>
    </div>

<!---->  </div>
</div>
</div>
        </li>
        <li class="pv-entity__position-group-role-item">
          <div id="ember805" class="ember-view"><div class="pv-entity__role-details">
  <span class="pv-entity__timeline-node"></span>
  <div class="display-flex justify-space-between full-width">
    <div class="pv-entity__role-container">
      <div class="pv-entity__role-details-container  ">

        <div class="pv-entity__summary-info-v2 pv-entity__summary-info--background-section pv-entity__summary-info-margin-top ">
          <h3 class="t-14 t-black t-bold">
            <span class="visually-hidden">Title</span>
            <span>IT Analyst</span>
          </h3>
<!---->            <div class="display-flex">
              <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
                <span class="visually-hidden">Dates Employed</span>
                <span>Aug 2015 – Present</span>
              </h4>
                <h4 class="t-14 t-black--light t-normal">
                  <span class="visually-hidden">Employment Duration</span>
                  <span class="pv-entity__bullet-item-v2">5 yrs 6 mos</span>
                </h4>
            </div>

<!----><!---->        </div>


<!---->      </div>
    </div>

<!---->  </div>
</div>
</div>
        </li>
    </ul>

<!----></section>
</li><li id="ember807" class="pv-entity__position-group-pager pv-profile-section__list-item ember-view">        <section id="500290588" class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
    <div class="display-flex flex-column full-width">
<a data-control-name="background_details_company" href="/company/wipro/" id="ember809" class="full-width ember-view">          <div class="pv-entity__logo company-logo">
  <img src="https://media-exp1.licdn.com/dms/image/C510BAQGmX81XFwCcFg/company-logo_100_100/0/1561636940118?e=1619654400&amp;v=beta&amp;t=20d17oeACkbpRX2QGLAf-_ZRWsEyt6hH-0N9VufIE0c" loading="lazy" alt="Wipro Technologies" id="ember811" class="pv-entity__logo-img EntityPhoto-square-5 lazy-image ember-view">
</div>
<div class="pv-entity__summary-info pv-entity__summary-info--background-section mb2">
  <h3 class="t-16 t-black t-bold">Technical Lead</h3>
  <p class="visually-hidden">Company Name</p>
  <p class="pv-entity__secondary-title t-14 t-black t-normal">
      Wipro Technologies
<!---->  </p>
    <div class="display-flex">
    <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates Employed</span>
      <span>Jan 2014 – Aug 2015</span>
    </h4>
      <h4 class="t-14 t-black--light t-normal">
        <span class="visually-hidden">Employment Duration</span>
        <span class="pv-entity__bullet-item-v2">1 yr 8 mos</span>
      </h4>
  </div>

  <h4 class="pv-entity__location t-14 t-black--light t-normal block">
    <span class="visually-hidden">Location</span>
    <span>Kolkata Area, India</span>
  </h4>

<!---->
</div>

</a>
        <div id="ember813" class="pv-entity__extra-details t-14 t-black--light ember-view"><p style="line-height:2rem;max-height:8rem;" id="ember814" class="pv-entity__description t-14 t-black t-normal inline-show-more-text inline-show-more-text--is-collapsed ember-view">  mobility practise of wipro technologies

<!----></p><!----></div>
    </div>

<!---->  </div>
</section>
</li><li id="ember816" class="pv-entity__position-group-pager pv-profile-section__list-item ember-view">        <section id="74112568" class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
    <div class="display-flex flex-column full-width">
<a data-control-name="background_details_company" href="/company/cris/" id="ember818" class="full-width ember-view">          <div class="pv-entity__logo company-logo">
  <img src="https://media-exp1.licdn.com/dms/image/C4E0BAQFcBMF23IdgNg/company-logo_100_100/0/1519856095392?e=1619654400&amp;v=beta&amp;t=00AmCRS4m-2LyiLDl_X_yspzVIZZpSR3RbKipD_59aU" loading="lazy" alt="Center For Railway Information Systems(CRIS),Under Ministry of Railways,Govt. of India" id="ember820" class="pv-entity__logo-img EntityPhoto-square-5 lazy-image ember-view">
</div>
<div class="pv-entity__summary-info pv-entity__summary-info--background-section mb2">
  <h3 class="t-16 t-black t-bold">Senior Software Engineer</h3>
  <p class="visually-hidden">Company Name</p>
  <p class="pv-entity__secondary-title t-14 t-black t-normal">
      Center For Railway Information Systems(CRIS),Under Ministry of Railways,Govt. of India
<!---->  </p>
    <div class="display-flex">
    <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates Employed</span>
      <span>Jul 2007 – Jan 2014</span>
    </h4>
      <h4 class="t-14 t-black--light t-normal">
        <span class="visually-hidden">Employment Duration</span>
        <span class="pv-entity__bullet-item-v2">6 yrs 7 mos</span>
      </h4>
  </div>

  <h4 class="pv-entity__location t-14 t-black--light t-normal block">
    <span class="visually-hidden">Location</span>
    <span>kolkata</span>
  </h4>

<!---->
</div>

</a>
        <div id="ember822" class="pv-entity__extra-details t-14 t-black--light ember-view"><p style="line-height:2rem;max-height:8rem;" id="ember823" class="pv-entity__description t-14 t-black t-normal inline-show-more-text inline-show-more-text--is-collapsed ember-view">  Sybase DBA,Sybase database developer,Sybase replication server,unix shell scripting,SQL Anywhere, SAP Sybase Unwired Platform,SAP SUP,linux administration,HP-UX administration

<!----></p><!----></div>
    </div>

<!---->  </div>
</section>
</li>  </ul>

<!----></section>
"""
#  t=BeautifulSoup(html,'html.parser').find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"})
def clean_string(var):
    var=str(var)
    var=var.strip()
    var=var.replace('\n','')
    return var
html_soup = BeautifulSoup(html_soup,'html.parser')
IDs = []
Defaults= []
Defaults = {'designation':'', 'company':'','dates_employed':'','employ_duration':''}
expdict = dict.fromkeys(IDs, Defaults)
name='aaa'
if name is not None :
	# print(expsect)
	i=0
	xx=html_soup.find("section", {"id":"experience-section"})
	print('@@@2'+xx.text)
	if(html_soup.find("section", {"class":"pv-profile-section experience-section ember-view"})):
	 expsect=html_soup.find("section", {"id":"experience-section"})
	 for k in expsect.find_all("section",{"pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view"}) :
            expdict[i]={'designation': clean_string(k.find("h3",{"class":"t-16 t-black t-bold"}).text) if k.find("h3",{"class":"t-16 t-black t-bold"}) else '',
                        'company': clean_string(k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}).text) if k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}) else '',
                        'employ_duration':clean_string(k.find("span",{"class":"pv-entity__bullet-item-v2"}).text) if k.find("span",{"class":"pv-entity__bullet-item-v2"}) else '',
                        'dates_employed': clean_string(k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"}).find("span",{"class":""}).text) if k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"}) else ''
                        }
            i=i+1 
for x, y in expdict.items():
    print(x, y)  
 
	